import time
import selenium
import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Safari()
driver.get('https://www.powerlanguage.co.uk/wordle/')


time.sleep(1)

Elem = driver.find_element(By.TAG_NAME, 'html')
Elem.click()

time.sleep(1)

Elem.send_keys('aeros')
Elem.send_keys(Keys.ENTER)
time.sleep(2)

row = driver.find_element(By.XPATH, '//*[@id="board"]/game-row[1]')

print(row)