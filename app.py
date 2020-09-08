import requests
import urllib.request
import time
import sys

from requests_html import HTMLSession
from bs4 import BeautifulSoup
from grubhub import Grubhub

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

url = 'https://www.grubhub.com/restaurant/okinawa-teriyaki-1100-western-ave-seattle/2064336'
# url = 'https://www.brainyquote.com/'

chrome_driver_path = '/Users/aidanmuller-cohn/Development/code/Slack_Bot/Lets-Eat/chromedriver'

chrome_options = Options()
chrome_options.add_argument('--headless')

webdriver = webdriver.Chrome(
  executable_path=chrome_driver_path, options=chrome_options
)

search_query = "life"

if (len(sys.argv) >= 2):
  search_query = sys.argv[1]
  print(search_query)


with webdriver as driver:
    # Set timeout time 
    wait = WebDriverWait(driver, 10)

    # retrive url in headless browser
    driver.get(url)
    
    # find search box
    # search = driver.find_element_by_id("hmSearch")
    # search.send_keys(search_query + Keys.RETURN)
    
    wait.until(presence_of_element_located((By.CLASS_NAME, "menu-group")))

    source = driver.page_source

    soup = BeautifulSoup(source)

    mydivs = soup.findAll('', {"class": "menuSection-title"})

    print(mydivs)

    # must close the driver after task finished
    driver.close()