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
		browser.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/button').click()
		carrusel = browser.find_elements(By.CSS_SELECTOR, ".andes-carousel-snapped__slide")
		self.assertGreater(len(carrusel),4)	
		
		

	def tearDown(self):
		self.browser.quit()

if __name__ == '__main__':
	unittest.main()