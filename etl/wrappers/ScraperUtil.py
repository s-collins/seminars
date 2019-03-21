from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='bs4')


class ScraperUtil:

	# seconds to wait to allow javascript to render
	SLEEP_AMOUNT = 1

	def __init__(self):

		# setup chrome driver
		options = webdriver.ChromeOptions()
		options.add_argument('--headless')
		options.add_argument('--no-sandbox')
		options.add_argument('--disable-dev-shm-usage')
		self.driver = webdriver.Chrome(chrome_options=options)
		self.driver.implicitly_wait(5)

	def __del__(self):

		# close chrome driver
		self.driver.quit()

	def GetHTML(self, url):
		"""
		Returns string containing HTML from given URL.
		"""
		self.driver.get(url)
		sleep(self.SLEEP_AMOUNT)
		body = self.driver.execute_script('return document.body')
		return body.get_attribute('innerHTML')

	def CssSelectFirst(self, html, css_selector):
		"""
		Returns the first node matching the given css selector.
		Returns 'None' if no node is found.
		"""
		soup = BeautifulSoup(html, features='html.parser')
		node = next(iter(soup.select(css_selector)), None)
		return str(node)

	def CssSelectMultiple(self, html, css_selector):
		"""
		Returns all nodes matching given css selector.
		Returns empty list if none found
		"""
		soup = BeautifulSoup(html, features='html.parser')
		soup_elements= soup.select(css_selector)
		elements = [str(node) for node in soup_elements]
		return elements

	def SelectElementsMulticlass(self, html, tag, css_class):
		"""
		Returns list of strings containing HTML of nodes with given CSS class.
		Returns empty list if no elements were found.
		"""
		soup = BeautifulSoup(html, features='html.parser')
		soup_elements = soup.find_all(
			tag,
			{'class': lambda x: x and css_class in x.split()}
		)
		elements = [str(node) for node in soup_elements]
		return elements

	def GetText(self, html):
		"""
		Returns text contained in given html tag.
		Removes leading and trailing whitespace.
		"""
		soup = BeautifulSoup(html, features='html.parser')
		text = soup.text.strip().encode('ascii', errors='ignore')
		return str(text.decode('ascii'))

	def GetAttribute(self, html, tag, attribute):
		"""
		Returns text value of a tag's particular attribute
		"""
		soup = BeautifulSoup(html, features='html.parser')
		attribute = soup.find(tag).get(attribute)
		return attribute
