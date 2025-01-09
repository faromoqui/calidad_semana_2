from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class eis_test(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Chrome()

	def test_load(self):
		browser = self.browser
		browser.get("https://www.tucarro.com.co/")
		self.assertIn("TuCarro", browser.title)
		self.assertIn("Colombia", browser.title)

	def tearDown(self):
		self.browser.quit()

if __name__ == '__main__':
	unittest.main()