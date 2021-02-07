import wikipedia
from openpyxl import Workbook

wikipedia.set_lang('th')
product = ['ทุเรียน','ลำไย','แอปเปิ้ล','มังคุด']


excelfile = Workbook()
sheet = excelfile.active #Sheet


sheet['B1'] = 'รายการผลไม้'

header = ['ลำดับ','สินค้า','ราคา','รายละเอียด']
sheet.append(header)

for i,pd in enumerate(product):
	content = wikipedia.summary(pd) #สรุป
	#content = wikipedia.page(pd).content
	row = [i+1, pd , 1000, content]
	sheet.append(row)

excelfile.save('fruit.xlsx')