from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import pause
import pynput
import os
from pynput.keyboard import Key, Controller
from datetime import datetime
#######YEAR#MONTH#DAY#HOUR#MINUTE###### DO NOT PUT ZERO BEFORE A NUMBER
# pause.until(datetime(2020, 3, 27, 11, 29))
# MAIL & PASSWORD (THE MAIL U WILL USE TO ENTER TO THE MEET)
usernameStr = 'yourgmailid'
passwordStr = 'password'
url_meet = 'https://meet.google.com/sqd-owmw-pyw'
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-infobars")
options.set_preference("permissions.default.microphone", 2)
options.set_preference("permissions.default.camera", 2)
browser =  webdriver.Firefox(options=options)
browser.set_window_size(800, 600)
browser.get(('https://accounts.google.com/ServiceLogin?'
             'service=mail&continue=https://mail.google'
             '.com/mail/#identifier'))
username = browser.find_element_by_id('identifierId')
username.send_keys(usernameStr)
nextButton = browser.find_element_by_id('identifierNext')
nextButton.click()
time.sleep(5)
keyboard = Controller()
password = browser.find_element_by_xpath("//input[@class='whsOnd zHQkBf']")
password.send_keys(passwordStr)
signInButton = browser.find_element_by_id('passwordNext')
signInButton.click()
time.sleep(3)
browser.get(url_meet)
time.sleep(10)
browser.find_element_by_xpath("//span[@class='NPEfkd RveJvd snByac' and contains(text(), 'Ask to join')]").click()
pause
