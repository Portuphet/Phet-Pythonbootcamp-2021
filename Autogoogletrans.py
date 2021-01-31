from google_trans_new import google_translator
from openpyxl import Workbook
from datetime import datetime

translator = google_translator ()
# result = translator.translate('cat', dest='th')
# print(result.text)
article = open('Article.txt', 'r')
article = article.read()
article = article.split()

result = []

for word in article:

	res = translator.translate([word],lang_tgt='th')
	resdel = res.strip(" [, ], ' ")
	print(resdel, type(resdel))

	result.append([word,resdel])

excelfile = Workbook()
sheet = excelfile.active

header = ['Vocab', 'Translate']
sheet.append(header)

for rs in result:
	sheet.append(rs)

dt = datetime.now().strftime('%Y-%m-%d %H%M%S')
excelfile.save('Vocab - {}.xlsx'.format(dt))





