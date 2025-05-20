from googletrans import Translator

translator = Translator()

# Example text to translate
text_to_translate = "Hello, how are you?"

# Translate to Hindi
translation = translator.translate(text_to_translate, dest='hi')

print("Original Text:", text_to_translate)
print("Translated Text:", translation.text)

