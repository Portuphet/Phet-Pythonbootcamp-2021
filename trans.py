from googletrans import Translator

translator = Translator ()

result = translator.translate('cat', dest='th')
print(result.text)