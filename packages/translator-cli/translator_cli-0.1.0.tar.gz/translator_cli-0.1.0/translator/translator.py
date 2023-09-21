import requests
import sys
from loguru import logger
from translator.consts import LIBRETRANSLATE_URL, LINGVANEX_CORRESPONDENCE

import io
text_trap = io.StringIO()
sys.stdout = text_trap
sys.stderr = text_trap
import translators as ts
sys.stdout = sys.__stdout__
sys.stderr = sys.__stderr__


def libre_translate(text, src, trg):
    data = {"q": text, "source": src, "target": trg}
    try:
        res = requests.post(LIBRETRANSLATE_URL, data=data).json()["translatedText"]
    except Exception as e:
        logger.exception("Something failed in the translation request")
        raise e
    return res


class Translator:
    def __init__(self, engine_list=None):
        if engine_list is None:
            self.engine_list = [
                "BING",
                "LINGVANEX",
                "REVERSO",
                "GOOGLE",
                "TENCENT",
                "LIBRETRANSLATE"
            ]
        else:
            self.engine_list = engine_list

    def translate(self, text, src, trg, engine=None, engine_index=0, debug=False):
        logger.debug(f"Text to translate: {text}")
        if engine is None:
            engine = self.engine_list[engine_index]

        try:
            if engine == "BING":
                r = ts.bing(text, from_language=src, to_language=trg)
                print("Using Bing engine")
            elif engine == "TENCENT":
                r = ts.tencent(text, from_language=src, to_language=trg)
                print("Using Tencent engine")
            elif engine == "LINGVANEX":
                r = ts.lingvanex(
                    text,
                    from_language=LINGVANEX_CORRESPONDENCE[src],
                    to_language=LINGVANEX_CORRESPONDENCE[trg]
                )
                print("Using Lingvanex engine")
            elif engine == "REVERSO":
                r = ts.reverso(text, from_language=src, to_language=trg)
                print("Using Reverso engine")
            elif engine == "GOOGLE":
                r = ts.google(text, from_language=src, to_language=trg)
                print("Using Google engine")
            else:
                r = ts.libre_translate(text, src, trg)
                print("Using Libretranslate engine")
        except Exception:
            if debug:
                logger.exception(f"Something failed with engine {engine}")
            if engine == self.engine_list[engine_index]:
                engine_index += 1
            r = self.translate(text, src, trg, engine_index=engine_index)
        return r
