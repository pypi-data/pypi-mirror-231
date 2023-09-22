import ast
import deepl
from typing import List

from logutils import get_logger
from chatgpt_klient.client import ChatGPTPrompt

from translator.consts import ENGINES, APP_NAME, GPT_ENGINES
from translator.utils import (
    language_pair_is_available,
    get_language_code,
    build_chatgpt_translation_prompt,
    get_prompt_for_batch_translation_by_doctype,
    set_logger_verbosity,
    build_system_directive_batch_translation_no_context,
)

# text_trap = io.StringIO()
# sys.stdout = text_trap
# sys.stderr = text_trap
#
# sys.stdout = sys.__stdout__
# sys.stderr = sys.__stderr__

logger = get_logger(APP_NAME)


class Translator:
    def __init__(self, engine_list=None, verbosity=1, openai_key=None, deepl_key=None):
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

    def translate(
        self, text: str, input_lang: str, output_lang: str, engine: str | None = None
    ) -> str:
        """
        Translate text using any of the supported engines in UlionTse's "translators"
        library. The function automatically tries to do its best to normalize the language
        codes so that the user does not have to worry about that.
        """
        engine = self.get_engine(engine)
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
        except Exception:
            logger.exception(
                f"Error when trying to translate {input_lang}->{output_lang} using {engine}"
            )
            logger.info("Retrying with the next engine available...")
            i = self.engine_list.index(engine)
            if (i + 1) >= len(self.engine_list):
                logger.error(
                    "No more engines available for performing this translation!"
                )
                raise Exception("No engine capable of performing the translation")
            else:
                r = self.translate(
                    text, input_lang, output_lang, self.engine_list[i + 1]
                )
        return r

    def batch_translate(
        self,
        texts: List[str],
        input_lang: str,
        output_lang: str,
        common_context: bool = False,
        engine: str | None = None,
        doctype: str | None = None,
    ):
        """
        Batch translation of a bunch of texts. This should grant a faster translation,
        reducing the overhead caused by the initialization processes. It also allows the
        app to consider all the texts provided as part of the same common text or context.
        This will probably enhance the obtained results. However, this option only makes
        sense with the "gpt3" and "gpt4" engines.
        """
        engine = self.get_engine(engine)
        translated_texts = []
        if common_context:
            logger.debug(f"Starting contextful batch translation with {engine}")
        else:
            logger.debug(f"Starting context-free batch translation with {engine}")

        if common_context and engine in ("gpt3", "gpt4"):
            if engine == "gpt3":
                gpt_engine = self.chatgpt3
            elif engine == "gpt4":
                gpt_engine = self.chatgpt4
            else:
                raise Exception("WTF")
            try:
                translated_texts = gpt_engine.send_prompt(
                    get_prompt_for_batch_translation_by_doctype(
                        texts, input_lang, output_lang, doctype=doctype
                    )
                )
                translated_texts = ast.literal_eval(translated_texts)
                if type(translated_texts) is not list or len(translated_texts) != len(
                    texts
                ):
                    logger.error(
                        f"Translation of strings with context failed.\nInput texts: {texts}\nOutput texts:{translated_texts}"
                    )
                    raise Exception(
                        f"Didn't get a well-formed list of translated texts"
                    )
            except Exception:
                translated_texts = self.batch_translate(
                    texts,
                    input_lang=input_lang,
                    output_lang=output_lang,
                    common_context=False,
                    engine=engine,
                )
        else:
            if engine in GPT_ENGINES:
                chatgpt = self.get_gpt_client(engine)
                sysdir = build_system_directive_batch_translation_no_context(
                    input_lang, output_lang
                )
                chatgpt.set_system_directive(sysdir)
            for t in texts:
                logger.debug(f"Translating text: {t}")
                if engine in GPT_ENGINES:
                    r = chatgpt.send_prompt(t, no_history=False)
                else:
                    r = self.translate(t, input_lang, output_lang, engine)
                logger.debug(f"Translation: {r}")
                translated_texts.append(r)

        logger.debug("Translations completed sucessfully")

        return translated_texts

    def get_engine(self, engine):
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
