from googletrans import Translator, LANGUAGES, LANGCODES

translator = Translator()


def TransLate(str, lang):
    try:
        return translator.translate(text=str, dest=lang).text
    except ValueError:
        return "Invalid destination language"


def LangDetect(txt):
    return translator.detect(txt)

def CodeLang(lang):
    lang = lang.lower()
    if LANGCODES.get(lang):
        return LANGCODES[lang]
    if LANGUAGES.get(lang):
        return LANGUAGES[lang]
    return lang

text = input("Enter string: ")
print(LangDetect(text))
language = input("Enter which language you want\nja,en,uk:\n")
print(CodeLang(language))
result = TransLate(text, language)
print(result)
