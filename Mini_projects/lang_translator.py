from translate import Translator
translator = Translator(to_lang = "french")
translation = translator.translate(input(" ENTER THE TEXT "))
print(translation)