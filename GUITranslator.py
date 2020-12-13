#GUItranslator.py
from tkinter import * #จากไลบรารีชื่อ tkinter, * ตือให้ดึงความสามารถหลักมาทังหมด
from tkinter import ttk # ttk is theme of tk
###--------------------------Google Translate----------------------
from googletrans import Translator
translator = Translator ( )      

GUI = Tk ( ) #สร้างหน้าต่างหลัก
GUI.geometry ( '500x300' ) #กว้าง x สูง
GUI.title ('โปรแกรมแปลภาษา by Phet THEPVONGSA' )
# --------------- Config------------------
FONT = ( ' Angsana New ' , 15 )

# --------------- Label-------------------
L = ttk.Label (GUI, text = 'กรุณากรอกคำศัพท์ที่ต้องการแปล', font=FONT)
L.pack ( pady=10 )

# ---------------Entry (ช่องกรอกข้อความ)-----------------
v_vocab = StringVar ( ) # กล่องเก็บข้อความ

E1 = ttk.Entry(GUI, textvariable = v_vocab, font=FONT) #สร้างช่องกรอกข้อความ และ กำหนดให้รับข้อความจากกล่องข้อความ
E1.pack (ipadx=40, ipady=5, pady=20) # show ช่่องกรอก

# ----------------Button--------------------
def Translate ( ):
      vocab = v_vocab.get ( ) # .get คือคำสั่งให้แสดงผลออกมาเนื่องจากไม่สามารถเรียนได้โดยตรง
      meaning = translator.translate ( vocab, dest = 'th' )
      print ( vocab + ' : ' + meaning.text )
      v_result.set ( meaning.text )

B1 = ttk.Button ( GUI,text = 'Translate', command=Translate ) #สร้างปุ่มขึ้นมา
B1.pack (ipadx=20, ipady=10 ) # show ปุ่มขึ้นมาวางจากบนลงล่าง

# --------------- Label-------------------
L = ttk.Label (GUI, text = 'คำแปล', font=FONT)
L.pack ( pady=20)

# --------------- Result------------------
v_result = StringVar ( )
FONT2 = ( ' Cordia New ' , 15)
E2 = ttk.Entry ( GUI, textvariable = v_result , font = FONT2 , foreground = 'green')
E2.pack ( ipadx = 40, ipady = 5)


GUI.mainloop ( ) # ทำให้โปรแกรมรันได้ตลอดเวลาจนกว่าจะปิด
