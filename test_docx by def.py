#test_docx by def.py
from docx import Document
import wikipedia

def wiki (keyword, lang='th'):
      wikipedia.set_lang(lang)
      # summary สำหรับบทความที่สรุป
      data = wikipedia.summary (keyword)

      # page + content บทความทังหน้า
      data2 = wikipedia.page(keyword)
      data2 = data2.content

      doc  = Document ( )
      doc.add_heading(keyword, 0)

      doc.add_paragraph(data2)
      doc.save(keyword + '.docx')
      print ('สร้างไฟล์สำเร็จ')

wiki ('ประเทศไทย')
wiki ('Lao', 'en')
wiki ('japan', 'jp')
