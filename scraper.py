# This will work using headless Chrome for any Desktop OS (Windows, MacOS, Linux Desktop)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import cv2
import numpy as np
import platform
import time
import string
import random


count = 0
#ID's of items
links = ['5687', '211', '18124', '6132']


images = []
# Gets the path to the right chromedriver
path = "C://Users//tyboe//Desktop//Programs//Python//rss//driver//chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_argument("headless")
# must install linux browser `sudo apt-get install -y chromium-browser` in Linux
options.binary_location = 'C://Program Files//BraveSoftware//Brave-Browser//Application//brave.exe'

options.add_argument("disable-infobars")  # disabling infobars
options.add_argument("--disable-extensions")  # disabling extensions
options.add_argument("--disable-gpu")  # applicable to windows os only
# overcome limited resource problems
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")  # Bypass OS security model

img = cv2.imread('0-ttc.png')
rows, cols, _ = img.shape
print('Rows', rows)
print('Cols', cols)

cut_image = img[635: 775, 35: 950]

cv2.imshow("Cut image", cut_image)
cv2.waitKey(0)


with webdriver.Chrome(path, chrome_options=options) as driver:
        # these values represent the sizes of the entire browser window and not the viewport.
        for link in links:
            tablet = {'output': str(count) + '-ttc.png',
                    'width': 1000,
                    'height': 800}
            post = str(count) + '-ttc.png'
            images.append(post)
            #Variable adds increments too change name of each screenshots too prevent duplicates
            count += 1
            #Main url
            linkWithProtocol = 'https://us.tamrieltradecentre.com/pc/Trade/SearchResult?ItemID=' + str(link) + '&SortBy=Price&Order=asc'
            #Sets browser size, gets Website, Takes Screenshot of the site
            driver.set_window_size(tablet['width'], tablet['height'])
            driver.get(linkWithProtocol)
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='search-result-view']/div[1]/div/table/tbody/tr[1]/td[4]")))
            driver.save_screenshot(tablet['output'])