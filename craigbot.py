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

        self.driver = webdriver.Chrome()
        self.delay = 3

    def load_craigslist_url(self):
        self.driver.get(self.url)
        try:
            wait = WebDriverWait(self.driver, self.delay)
            wait.until(EC.presence_of_element_located((By.ID, "searchform")))
            print("page is ready")
        except TimeoutException:
            print("loading took too much time")

    def extract_post_information(self):

        all_posts = self.driver.find_elements_by_class_name("result-row")
        #print(all_post)
        post_title_list = []
        for post in all_posts:
            #print(post.text)
            title = post.text.split("$")

            if title[0] == '':
                title = title[1]
            else:
                title=title[0]

            title = title.split("\n")
            price = title[0]
            title = title[-1]
            date = title.split(" ")
            month = date[0]
            day = date[1]
            date = month + " " + day

            print("title: " +title)
            print("price: "+price)
            print("date: " +date)
            print("\n")
            post_title_list.append(post.text)
        return post_title_list

    def extract_post_urls(self):
        url_list = []
        html_page = urllib.request.urlopen(self.url)
        soup = BeautifulSoup(html_page, 'lxml')
        for link in soup.findAll("a", {"class":"result-title hdrlink"}):
            print(link)
            url_list.append(link["href"])
        return(url_list)

    def quit(self):
        self.driver.close()


location = "sfbay"
postal="94201"
max_price = "500"
radius = "5"


scraper = CraigslistScraper(location, postal, max_price, radius)
scraper.load_craigslist_url()
scraper.extract_post_information()
#scraper.extract_post_urls()
scraper.quit()
