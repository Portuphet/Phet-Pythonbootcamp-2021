## autobrowserbbc.py
import webbrowser
import pyautogui as pg # nickname is pg
import time
import pyperclip
from datetime import datetime

def ScanBBC(scroll=False, sctime=10):
	## 1- open webbrowser and goto google
	url = 'https://www.bbc.com'
	webbrowser.open(url)
	time.sleep(2) # delay after open webbrowser
	dt = datetime.now().strftime('%Y-%m-%d %H%M%S')

	## 2- capture (screenshot) and save to file
	if scroll == True:
		for i in range(sctime):
			time.sleep(3)
			pg.screenshot( '{}-{}.png'.format('BBC'+dt, i+1))
			pg.scroll(-700)
			
	else:
		pg.screenshot( 'BBC'+ dt + '.png')

ScanBBC(scroll=True)
