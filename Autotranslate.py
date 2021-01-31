from easyread.translator import Translate
from openpyxl import Workbook
from datetime import datetime


# result = translator.translate('cat', dest='th')
# print(result.text)
article = open('Article.txt', 'r')
article = article.read()
article = article.split()

print('Count: ', len(article))
result = []

for word in article:

	res = Translate(word)
	if res != None:

		result.append([word,res['meaning']])

excelfile = Workbook()
sheet = excelfile.active

header = ['Vocab', 'Translate']
sheet.append(header)

for rs in result:
	sheet.append(rs)

dt = datetime.now().strftime('%Y-%m-%d %H%M%S')
excelfile.save('Vocab - {}.xlsx'.format(dt))


