from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup
import urllib.request

class CraigslistScraper(object):
    def __init__(self, location, postal, max_pirce, radius):
        self.location = location
        self.postal = postal
        self.max_price = max_price
        self.radius = radius

        #search_distance=5&postal=60649&max_price=500

        self.url = f"https://{location}.craigslist.org/search/sss?/search_distance={radius}&postal={postal}&max_price={max_price}"

    def test(self):
        print(self.url)

location = "sfbay"
postal="94201"
max_price = "500"
radius = "5"


scraper = CraigslistScraper(location, postal, max_price, radius)
scraper.test()
