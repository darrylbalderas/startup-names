from googletrans import Translator
from googletrans.constants import LANGUAGES, LANGCODES

import argparse

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


def setup_parser():
    parser = argparse.ArgumentParser(description='Translate word in top 14 languages')
    parser.add_argument('word', type=str,
                        help='Word you wish to translate in top 14 languages')

    return parser


def main():
    args = setup_parser().parse_args()
    translator = Translator()
    word = args.word
    print(f"Original word :{word}")
    print("------------")
    for index, l in enumerate(top_languages):
        language, code = l
        translate_word = translator.translate(word, dest=code)
        print(f"{index + 1}. {language} translated word : {translate_word.text}")


if __name__ == '__main__':
    main()
