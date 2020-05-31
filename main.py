from googletrans import Translator
from googletrans.constants import LANGUAGES, LANGCODES

import argparse
import logging
import sys


top_languages = [(t.lower(), LANGCODES[t.lower()]) for t in [
      "chinese (traditional)",
      "chinese (simplified)",
      "hindi",
      "Spanish",
      "Arabic",
      "Malay",
      "Russian",
      "Bengali",
      "Portuguese",
      "French",
      "Hausa",
      "Punjabi",
      "Telugu",
      "Javanese"
]]

def setup_logger():
    logger = logging.getLogger("translate")
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def setup_parser():
    parser = argparse.ArgumentParser(description='Translate word in top 14 languages')
    parser.add_argument('word', type=str,
                        help='Word you wish to translate in top 14 languages')

    return parser


def main():
    logger = setup_logger()
    args = setup_parser().parse_args()
    translator = Translator()
    word = args.word
    logger.info(f"Original word :{word}")
    logger.info("------------")
    for index, l in enumerate(top_languages):
        language, code = l
        translate_word = translator.translate(word, dest=code)
        logger.info(f"{index + 1}. {language} translated word : {translate_word.text}")


if __name__ == '__main__':
    main()
