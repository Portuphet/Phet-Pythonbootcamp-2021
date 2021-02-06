## autobrowser.py
import webbrowser
import pyautogui as pg # nickname is pg
import time

def Search(keyword):
	## 1- open webbrowser and goto google
	url = 'https://www.google.com'
	webbrowser.open(url)
	time.sleep(2) # delay after open webbrowser

	## 2- type "keyword"
	pg.write(keyword, interval = 0.25)
	time.sleep(1)

	## 3- press enter for searching
	pg.press('enter')
	time.sleep(2)

	## 4- capture (screenshot) and save to file
	pg.screenshot( keyword + '.png')

Search('facebook')


