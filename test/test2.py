from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest


class eis_test(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Chrome()

	def test_load(self):
		browser = self.browser
		browser.get("https://www.tucarro.com.co/")
		time.sleep(2)
		browser.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/div[3]/a').click()
		self.assertIn("Carros", browser.title)
		self.assertIn("Camionetas", browser.title)


		

	def tearDown(self):
		self.browser.quit()

if __name__ == '__main__':
	unittest.main()