import time
import selenium
import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Safari()
browser.get('https://www.powerlanguage.co.uk/wordle/')

def make_initial_guesses():
    words = ['quick', 'brown', 'shady', 'cleft', 'gimps']

    time.sleep(1)

    Elem = browser.find_element(By.TAG_NAME, 'html')
    Elem.click()

    time.sleep(1)
    
    for word in words:
        Elem.send_keys(word)
        Elem.send_keys(Keys.ENTER)
        time.sleep(2)

def get_key_data():
    game_app = browser.find_element(By.TAG_NAME, "game-app")
    game = browser.execute_script("return arguments[0].shadowRoot.getElementById('game')", game_app)
    game_row = browser.execute_script("return arguments[0].innerHTML;",game.find_element(By.TAG_NAME, "game-row"))

    print(game_row)

def sort_key_data(keydata):
    absent_letters = re.findall('(.).{14}abs', keydata)
    present_letters = re.findall('(.).{14}pre', keydata)
    correct_letters = re.findall('(.).{14}cor', keydata)
    print(absent_letters)

make_initial_guesses()
keydata = get_key_data()
#sort_key_data(keydata)