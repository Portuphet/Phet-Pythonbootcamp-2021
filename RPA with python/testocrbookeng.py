## ocrbookeng.py

from PIL import Image
import pytesseract

#pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe" #first time when install tesseract must be add this line at first time when run code
print(pytesseract.image_to_string(Image.open('book2.jpg')))