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
		buscador = browser.find_element(By.XPATH, '/html/body/header/div/form/input')
		buscador.clear()
		buscador.send_keys('honda crv')
		
		buscador.send_keys(Keys.ENTER)
		
		resultado = browser.find_element(By.XPATH, '/html/body/main/div/div[3]/section/ol/li[1]/div/div/div[2]/h2/a')
		self.assertIn('Cr-v',resultado.text )

	def tearDown(self):
		self.browser.quit()

if __name__ == '__main__':
	unittest.main()