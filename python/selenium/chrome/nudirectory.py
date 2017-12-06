# From https://duo.com/blog/driving-headless-chrome-with-python
from io import StringIO
import os
from pprint import pprint
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from lxml import etree

class NUDirectoryDriver(object):

    def __init__(self):
        self.BASE_URL = 'http://directory.northwestern.edu/?verbose=1'

    def init(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.binary_location = '/usr/bin/google-chrome'
        self.driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"), chrome_options=chrome_options)
        self.driver.get(self.BASE_URL)

    def __enter__(self):
        self.init()
        return self.driver

    def __exit__(self, *args):
        self.driver.close()


if __name__=="__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("python %s netid" % __file__)
        sys.exit(1)

    netid = sys.argv[1]
    nudirectory = NUDirectoryDriver()
    nudirectory.init()
    driver = nudirectory.driver
    driver.find_element_by_css_selector('input[name=query]')
    query = driver.find_element_by_css_selector('input[name=query]')
    query.send_keys("netid=%s" % (netid))
    search_button = driver.find_element_by_css_selector('input[value=Search]')
    search_button.click()
    more_link = driver.find_element_by_css_selector('a[alt=more]')
    more_link.click()
    html = driver.page_source
    driver.close()

    htmlparser = etree.HTMLParser()
    tree = etree.parse(StringIO(html), htmlparser)
    div = tree.xpath('//*[@id="main-content"]/div[2]/div/table/tbody/tr[2]/td/div')[0]

    soup = BeautifulSoup(etree.tostring(div), 'lxml')
    details = {}
    for row in soup.find_all('tr'):
        key_element, val_element = row.find_all('td')
        details[key_element.text] = val_element.text

    pprint(details)
