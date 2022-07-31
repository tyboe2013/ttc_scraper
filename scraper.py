# This will work using headless Chrome for any Desktop OS (Windows, MacOS, Linux Desktop)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import cv2
import numpy as np
import platform
import time
import string
import random
import pytesseract

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
coordinates = []
def shape_selection(event, x, y, flags, param):
    global coordinates
    if event == cv2.EVENT_LBUTTONDOWN:
        coordinates = [(x, y)]
    elif event == cv2.EVENT_LBUTTONUP:
        coordinates.append((x,y))
        cv2.rectangle(img, coordinates[0],coordinates[2], (0,0,255),2)
        cv2.imshow('image', img)

img = cv2.imread('0-ttc.png')
cv2.namedWindow('img')
cv2.setMouseCallback('img', shape_selection)
rows, cols, _ = img.shape

cut_image = img[635: 775, 35: 950]
cv2.imwrite('ttc.png', cut_image)
cv2.waitKey(0)
crop = cv2.imread('ttc.png')
crop_copy = crop.copy()
config = ('-l eng --oem 1 --psm 3')
pytesseract.pytesseract.tesseract_cmd = 'C://Program Files//Tesseract-OCR//tesseract.exe'
text = pytesseract.image_to_string(crop, config=config)

while (True):
    cv2.imshow('crop', crop)
    key = cv2.waitKey(1) & 0xFF

    if key==13:
        break
    if key == ord('c'):
        crop = crop_copy.copy()


if len(coordinates) == 2:
    image_roi = crop_copy[coordinates[0][1]:coordinates[1][1],
                                coordinates[0][0]:coordinates[1][0]]
    cv2.show('roi press any key', image_roi)
