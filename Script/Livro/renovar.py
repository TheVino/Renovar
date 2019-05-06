from selenium import webdriver
import time
#from bs4 import BeautifulSoup
#import requests
#import pynput

driver = webdriver.Chrome()

driver.set_page_load_timeout(10)
driver.get("http://sofia.fei.edu.br/pergamum/biblioteca/index.php")
driver.find_element_by_id("div_login").click()
time.sleep(4)
driver.quit()


#url = requests.get('http://sofia.fei.edu.br/pergamum/biblioteca/index.php')

#soup = BeautifulSoup(url.text, 'html.parser')

#with open('sb.txt' , 'w') as f:
#	for subreddit in soup.find_all('a'):
#		try:
#			if 'r' in subreddit.string:
#				f.write(subreddit.string[0:] + '\n')
#		except:
#				TypeError	