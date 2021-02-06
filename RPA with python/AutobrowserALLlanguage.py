## autobrowserALLlanguage.py
import webbrowser
import pyautogui as pg # nickname is pg
import time
import pyperclip

def Search(keyword, eng=False, scroll=False, sctime=10):
	## 1- open webbrowser and goto google
	url = 'https://www.google.com'
	webbrowser.open(url)
	time.sleep(2) # delay after open webbrowser

	## 2- type "keyword"
	if eng == True:
		pg.write(keyword, interval=0.25)
	else:
		pyperclip.copy(keyword)
		time.sleep(1)
		pg.hotkey('ctrl', 'v')

	time.sleep(1)

	## 3- press enter for searching
	pg.press('enter')
	time.sleep(2)

	## 4- capture (screenshot) and save to file
	if scroll == True:
		for i in range(sctime):
			pg.scroll(-500)
			pg.screenshot( '{}-{}.png'.format(keyword, i+1))
			time.sleep(1)
	else:
		pg.screenshot( keyword + '.png')

Search('ราคาน้ำมัน', scroll=True)
