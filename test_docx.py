#test_docx.py
from docx import Document
import wikipedia
wikipedia.set_lang ('th')

# summary สำหรับบทความทีสรุป
data = wikipedia.summary ('งู')

# page + content บทความทังหน้า
data2 = wikipedia.page ('งู')
data2 = data2.content

doc = Document ( ) # สร้างไฟล์ word ใน python
doc.add_heading ('งู' , 0)

doc.add_paragraph(data2)
doc.save ('งู.docx')
print ('สร้างไฟล์สำเร็จ')
