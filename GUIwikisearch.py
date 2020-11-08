###----------------WikisearchProgram------------------####
import wikipedia
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
GUI = Tk ( )
GUI.title ('โปรแกรม wiki by Phet THEPVONGSA')
GUI.geometry ('400x300')
###---------------Python to docx-----------------------####
from docx import Document

def wiki (keyword, lang='th'):
      wikipedia.set_lang(lang)
      # summary สำหรับบทความที่สรุป
      data = wikipedia.summary (keyword)

      doc  = Document ( )
      doc.add_heading(keyword, 0)

      doc.add_paragraph(data)
      doc.save(keyword + '.docx')
      print ('สร้างไฟล์สำเร็จ')

#------------------Configเปลี่ยนเป็นภาษาไทย------------------
wikipedia.set_lang('th')
FONT1 =  ( 'Cordia New' , 15)

#------------------Discription for search----------------------
L1 = ttk.Label(GUI, text = 'ค้าหาบทความ' , font=FONT1)
L1.pack ( )

#------------------Searchbox------------------------------------
v_search = StringVar ( )
E1 = ttk.Entry (GUI, textvariable = v_search, font=FONT1, width=40)
E1.pack (pady=10)

#------------------Button-----------------------------------------
def Search ( ):
      keyword = v_search.get ( )
      try:
            # ลองค้นหาดูว่าได้ผลลัพท์หรือไม่ หากไม่ได้ให้ผ่านไป
            language = v_radio.get ( ) #th / en / zh
            wiki (keyword)
            messagebox.showinfo('บันทึกสำเร็จ','ค้นหาข้อมูลสำเร็จ บันทึกเรียบร้อยแล้ว')
      except:
            # หากรันคคำสั่งแล้วมีปัญหา แสดงข้อความแจ้งเตือน
            messagebox.showwarning('Keyword error', 'กรุณากรอกคำค้นหาใหม่')
      #print (wikipedia.search (keyword))
      #result = wikipedia.summary (keyword)
      #print (result)
      
B1 = ttk.Button (GUI, text = 'search' , command = Search)
B1.pack(ipadx=20, ipady=10)

# เลือกภาษา
F1 = Frame (GUI)
F1.pack (pady=10)

v_radio = StringVar ( ) # ช่องเก็บข้อมูลเลือกภาษา

RB1 = ttk.Radiobutton (F1, text='ภาษาไทย', variable=v_radio, value='th')
RB2 = ttk.Radiobutton (F1, text='English', variable=v_radio, value='en')
RB3 = ttk.Radiobutton (F1, text='中文', variable=v_radio, value='zh')

RB1.invoke ( )

RB1.grid (row=0, column=0 )
RB2.grid(row=0, column=1)
RB3.grid(row=0, column=2)


GUI.mainloop ( )
