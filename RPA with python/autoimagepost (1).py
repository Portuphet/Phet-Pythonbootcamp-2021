# autoimagepost.py

import os
import wikipedia
import time
wikipedia.set_lang('th')

imgfile = os.listdir()
print(imgfile)
print('------')
#######################################
wordlist = []

for img in imgfile:
	if img[-3:] == 'jpg' or img[-3:] == 'png':
		# [-3:] คือ 3 ตัวสุดท้าย
		#print(img)
		fn = img.split('.')[0]
		wordlist.append(fn)


alltitle = []
alldata = []

for wl in wordlist:
	data = wikipedia.summary(wl)
	page = wikipedia.page(wl)
	title = page.title

	alltitle.append(title)
	alldata.append(data)
	print('Topic: {}'.format(title))
	print(data)
	print('===============')
	print('----------')

#######################################


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driverpath = r'C:\Users\Uncle Engineer\Desktop\Python Bootcamp 2021\Class Main\EP3\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(driverpath)

url = 'http://www.uncle-machine.com/login/'

driver.get(url)


username = driver.find_element_by_id('username')
username.send_keys('loong9999@gmail.com')

password = driver.find_element_by_id('password')
password.send_keys('1234')
password.send_keys(Keys.RETURN) # press enter after type password

#button = driver.find_element_by_xpath('/html/body/div[2]/form/button')
#button.click()

addurl = 'http://www.uncle-machine.com/addproduct/'

driver.get(addurl) # goto addurl

# add product

pdname = driver.find_element_by_id('name')
pdprice = driver.find_element_by_id('price')
pddetail = driver.find_element_by_id('detail')
photo = driver.find_element_by_id('photo')

pd1_name = alltitle[1]
pd1_price = 1000
pd1_detail = alldata[1]
photopath = r'C:\Users\Uncle Engineer\Desktop\Python Bootcamp 2021\Class Main\EP4\ipad.jpg'

pdname.send_keys(pd1_name)
pdprice.send_keys(pd1_price)
pddetail.send_keys(pd1_detail)
photo.send_keys(photopath)
time.sleep(5)

button = driver.find_element_by_xpath('/html/body/div[2]/form/button')
button.click()

