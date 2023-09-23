import ast
import deepl
from typing import List, Literal

from logutils import get_logger
from chatgpt_klient.client import ChatGPTPrompt

from translator.consts import ENGINES, APP_NAME, GPT_ENGINES
from translator.utils import (
    language_pair_is_available,
    get_language_code,
    build_chatgpt_translation_prompt,
    get_prompt_by_doctype,
    set_logger_verbosity,
    build_system_directive_batch_translation_no_context,
    structure_equals,
)
from translator.exceptions import MalformedResponseError

# text_trap = io.StringIO()
# sys.stdout = text_trap
# sys.stderr = text_trap
#
# sys.stdout = sys.__stdout__
# sys.stderr = sys.__stderr__

logger = get_logger(APP_NAME)


class Translator:
    def __init__(
        self,
        engine_list: List | None = None,
        verbosity=1,
        openai_key=None,
        deepl_key=None,
    ):
        set_logger_verbosity(verbosity)
        if engine_list is None:
            self.engine_list = ENGINES
        else:
            self.engine_list = engine_list
        if "deepl" in self.engine_list and deepl_key is not None:
            try:
                self.deepl_translator = deepl.Translator(deepl_key)
            except Exception:
                logger.exception("Could not configure DeepL engine.")
                self.engine_list.remove("deepl")
        if "gpt3" in self.engine_list and openai_key is not None:
            try:
                self.chatgpt3 = ChatGPTPrompt(
                    api_key=openai_key, engine="gpt-3.5-turbo-16k"
                )
            except Exception:
                logger.exception("Could not configure GPT3 engine.")
                self.engine_list.remove("gpt3")
        if "gpt4" in self.engine_list and openai_key is not None:
            try:
                self.chatgpt4 = ChatGPTPrompt(api_key=openai_key, engine="gpt-4")
            except Exception:
                logger.exception("Could not configure GPT4 engine.")
                self.engine_list.remove("gpt4")
        if "google" in self.engine_list:
            from googletrans import Translator as GoogleTranslator

            self.gtranslator = GoogleTranslator()

    def translate(
        self,
        text: str,
        input_lang: str,
        output_lang: str,
        retry_next_engine: bool = True,
    ) -> str:
        """
        Translate text using any of the supported engines in UlionTse's "translators"
        library. The function automatically tries to do its best to normalize the language
        codes so that the user does not have to worry about that.
        """
        if text.strip() == "":
            return text
        engine = self.get_engine(None)
        try:
            if language_pair_is_available(engine, input_lang, output_lang) is False:
                logger.error(f"{input_lang}->{output_lang} unavailable for {engine}")
                raise Exception(f"{input_lang}->{output_lang} unavailable for {engine}")
            if engine == "deepl":
                r = self.deepl_translator.translate_text(
                    text, source_lang=input_lang, target_lang=output_lang
                ).text  # type: ignore
            elif engine == "gpt3":
                text = build_chatgpt_translation_prompt(text, input_lang, output_lang)
                r = self.chatgpt3.send_prompt(text, no_history=True)
            elif engine == "gpt4":
                text = build_chatgpt_translation_prompt(text, input_lang, output_lang)
                r = self.chatgpt4.send_prompt(text, no_history=True)
            elif engine == "google":
                r = lambda x: self.gtranslator.translate(
                    x, src=input_lang, dest=output_lang
                ).text
            else:
                import translators as ts

                r = ts.translate_text(
                    text,
                    translator=engine,
                    from_language=get_language_code(input_lang, engine),
                    to_language=get_language_code(output_lang, engine),
                )
            logger.info(f"Text translated using {engine}")
            if type(r) is not str:
                raise Exception
        except Exception as e:
            logger.exception(
                f"Error when trying to translate {input_lang}->{output_lang} using {engine}"
            )
            if retry_next_engine:
                logger.info("Retrying with the next engine available...")
                i = self.engine_list.index(engine)
                if (i + 1) >= len(self.engine_list):
                    logger.error(
                        "No more engines available for performing this translation!"
                    )
                    raise Exception("No engine capable of performing the translation")
                else:
                    r = self.translate(text, input_lang, output_lang, retry_next_engine)
            else:
                raise e
        if not isinstance(r, str):
            raise Exception(f"Returned object should be a string, but it is: {r}")
        return r

    def custom_translation(
        self,
        data: str,
        input_lang: str,
        output_lang: str,
        engine: str | None,
        doctype: str | None = None,
    ):
        """
        Perform a translation of anything using ChatGPT. This function will take pass what is
        received in the "data" parameter and insert it in a ChatGPT prompt. Thus, te real relevant
        information for getting a good translation is in the prompt. The function can select one
        prompt or another depending on the type of document, and complete it with the origin and
        target languages.
        Data should be a Python data structure
        """
        engine = self.get_engine(engine)
        if engine == "gpt3":
            gpt_engine = self.chatgpt3
        elif engine == "gpt4":
            gpt_engine = self.chatgpt4
        else:
            raise Exception(
                f"Custom translation only allowed for LLM-based engines: {GPT_ENGINES}"
            )
        prompt = get_prompt_by_doctype(data, input_lang, output_lang, doctype)
        translation = gpt_engine.send_prompt(prompt)
        try:
            translation = ast.literal_eval(translation)
            if not structure_equals(data, translation):
                raise Exception(f"Didn't get a well-formed list of translated texts")
        except Exception:
            logger.exception(f"Results are malformed and cannot be used: {translation}")
            raise MalformedResponseError("Malformed results from ChatGPT")
        return translation

    def batch_translate(
        self,
        texts: List[str],
        input_lang: str,
        output_lang: str,
        retry_next_engine: bool = True,
    ):
        """
        Batch translation of a bunch of texts. This should grant a faster translation,
        reducing the overhead caused by the initialization processes.
        """
        engine = self.get_engine(None)
        translated_texts = []
        logger.debug(f"Starting context-free batch translation with {engine}")

        if engine in GPT_ENGINES:
            chatgpt = self.get_gpt_client(engine)
            sysdir = build_system_directive_batch_translation_no_context(
                input_lang, output_lang
            )
            chatgpt.set_system_directive(sysdir)
            translate_fn = lambda x: chatgpt.send_prompt(x, no_history=False)
        elif engine == "google":
            translate_fn = lambda x: self.gtranslator.translate(
                x, src=input_lang, dest=output_lang
            ).text
        else:
            translate_fn = lambda x: self.translate(
                x, input_lang, output_lang, retry_next_engine
            )
        translated_texts = translate_nested_lists(texts, translate_fn)
        logger.debug("Translations completed sucessfully")

        return translated_texts

    def get_engine(self, engine: str | None) -> str:
        if engine is None:
            engine = self.engine_list[0]
        elif engine not in self.engine_list:
            raise Exception(
                f"Translator object wasn't initialized with support for {engine} engine. "
                f"Available engines are the following ones: {self.engine_list}"
            )
        return engine

    def get_gpt_client(self, engine):
        if engine == "gpt3":
            return self.chatgpt3
        elif engine == "gpt4":
            return self.chatgpt4
        else:
            raise Exception(f"{engine} is not a valid GPT engine")


def translate_nested_lists(lst: List, translate_fn):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.append(translate_nested_lists(item, translate_fn))
        elif isinstance(item, str):
            logger.debug(f"Translating: {item}")
            if item.strip() == "":
                r = item
            else:
                try:
                    r = translate_fn(item)
                except Exception as e:
                    logger.exception(
                        f"Something failed when translating this string: '{item}'"
                    )
                    r = item
            result.append(r)
            logger.debug(f"Translation: {r}")
        else:
            raise Exception(
                "Can only translate data structures formed by strings as terminal nodes"
            )
    return result
