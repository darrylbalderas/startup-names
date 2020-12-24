from googletrans import Translator
from googletrans.constants import LANGUAGES, LANGCODES
from src.common import SUPPORTED_LANGUAGES

import argparse
import logging
import sys


def setup_logger():
    logger = logging.getLogger("translate")
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def setup_parser():
    parser = argparse.ArgumentParser(description='Translate word in top 14 languages')
    parser.add_argument('word',
                        type=str,
                        help='Word you wish to translate in top 14 languages')
    return parser


def main():
    logger = setup_logger()
    args = setup_parser().parse_args()
    translator = Translator()
    logger.info(f"Original word : {args.word}")
    for i, l in enumerate(SUPPORTED_LANGUAGES):
        translate_word = translator.translate(args.word, dest=l.code)
        logger.info(f"{i + 1}. {l.name} translated word : {translate_word.text}")
