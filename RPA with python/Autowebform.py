## Autowebform.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driverpath = r'C:/Users/ASUS/Desktop/Phet-Pythonbootcamp-2021/RPA with python/msedgedriver.exe'
driver = webdriver.Edge(driverpath)

url = 'http://uncle-machine.com/login/'

driver.get(url)


username = driver.find_element_by_id('username')
username.send_keys('portuphet@hotmail.com')

password = driver.find_element_by_id('password')
password.send_keys('9891')
#password.send_keys(Keys.RETURN) # press enter after type password

loginButton = driver.find_element_by_xpath('/html/body/div[2]/form/button')
loginButton.click()

addurl = 'http://uncle-machine.com/addproduct/'

driver.get(addurl) # goto addurl

## add product

pdname = driver.find_element_by_id('name')
pdprice = driver.find_element_by_id('price')
pddetail = driver.find_element_by_id('detail')

pd1_name = 'ทุเรียนจากเซี่ยงไฮ้2'
pd1_price = 1000
pd1_detail = ''' ทุเรียน เป็นไม้ผลในวงศ์ฝ้าย (Malvaceae) ในสกุลทุเรียน (Durio)[2][1] 
(ถึงแม้ว่านักอนุกรมวิธานบางคนจัดให้อยู่ในวงศ์ทุเรียน (Bombacaceae)[3] ก็ตาม[1]) 
เป็นผลไม้ซึ่งได้ชื่อว่าเป็นราชาของผลไม้[4][5][6] ผลทุเรียนมีขนาดใหญ่และมีหนามแข็งปกคลุมทั่วเปลือก 
อาจมีขนาดยาวถึง 30 ซม. และอาจมีเส้นผ่าศูนย์กลางยาวถึง 15 ซม. โดยทั่วไปมีน้ำหนัก 1-3 กิโลกรัม 
ผลมีรูปรีถึงกลม เปลือกมีสีเขียวถึงน้ำตาล เนื้อในมีสีเหลืองซีดถึงแดง แตกต่างกันไปตามสปีชีส์
'''

pdname.send_keys(pd1_name)
pdprice.send_keys(pd1_price)
pddetail.send_keys(pd1_detail)


submitButton = driver.find_element_by_xpath('/html/body/div[2]/form/button')
submitButton.click()

