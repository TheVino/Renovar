from selenium import webdriver
import time
import getpass
import os
import unittest
import HtmlTestRunner

class GoogleSearch(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		h = getpass.getuser()
		dir = os.path.join(r'C:\Users\{}\Desktop\Script\drivers\chromedriver_win32\chromedriver.exe'.format(h))
		cls.driver = webdriver.Chrome(dir)
		cls.driver.implicitly_wait(10)
		cls.driver.maximize_window()

	def test_search_google(self):
		self.driver.get("https://google.com")
		self.driver.find_element_by_name("q").send_keys("Test selenium")
		self.driver.find_element_by_name("btnK").click()

	def test_search_openvino(self):
		self.driver.get("https://google.com")
		self.driver.find_element_by_name("q").send_keys("whats open vino?")
		self.driver.find_element_by_name("btnK").click()
	@classmethod
	def tearDownClass(cls):
		cls.driver.close()
		cls.driver.quit()
if __name__ == '__main__':
	unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/vlopessi/Desktop/Script'))
# >> cd C:\Users\vlopessi\Desktop\Script
# >> C:\Users\vlopessi\Desktop\Script>python -m unittest teste.py
#https://www.youtube.com/watch?v=H9HUVSA_78U