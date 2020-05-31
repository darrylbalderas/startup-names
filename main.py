from googletrans import Translator
translator = Translator()
translations = translator.translate(['The quick brown fox', 'jumps over', 'the lazy dog'], dest='ko')

for t in translations:
    print(t.origin, t.text)
