from googletrans import Translator
from editor import captions
translator = Translator()

translation = translator.translate(captions,dest="hi")
print(translation)