from googletrans import Translator
from googletrans.constants import LANGUAGES, LANGCODES


def main():
    translator = Translator()
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
    print(f"Original word :{word}")
    print("------------")
    for index, l in enumerate(top_languages):
        language, code = l
        translate_word = translator.translate(word, dest=code)
        print(f"{index + 1}. {language} translated word : {translate_word.text}")


if __name__ == '__main__':
    main()
