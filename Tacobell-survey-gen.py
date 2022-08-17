from argparse import Action
import os
import time
import json
from webbrowser import Chrome
import gspread
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
import random

def openSurvey():
    global driver, code_one, code_two, code_three, code_four
    code_one = "0258"
    code_two = "0033"
    code_three = "1896"
    code_four = random.randint(2415,4000)
    chrome_service = Service('chromedriver')
    driver = webdriver.Chrome(service=chrome_service)
    driver.get("https://tellthebell.com/?AspxAutoDetectCookieSupport=1")
    time.sleep(2)
    try:
        CN1 = driver.find_element(By.XPATH, "//input[@name='CN1']")
        CN2 = driver.find_element(By.XPATH, "//input[@name='CN2']")
        CN3 = driver.find_element(By.XPATH, "//input[@name='CN3']")
        CN4 = driver.find_element(By.XPATH, "//input[@name='CN4']")
        Start = driver.find_element(By.XPATH, "//input[@name='NextButton']")
        ActionChains(driver)\
            .send_keys_to_element(CN1, code_one)\
            .send_keys_to_element(CN2, code_two)\
            .send_keys_to_element(CN3, code_three)\
            .send_keys_to_element(CN4, code_four)\
            .click(Start)\
            .perform()
        time.sleep(1)
        Highlysatisfied = driver.find_element(By.XPATH, "//td[@class='Opt5 inputtyperbloption']")
        Nextbutton = driver.find_element(By.XPATH, "//input[@class='NextButton']")
        ActionChains(driver)\
            .click(Highlysatisfied)\
            .click(Nextbutton)\
            .perform()
        time.sleep(1)  
        Highlysatisfieds = driver.find_elements(By.XPATH, "//td[@class='Opt5 inputtyperbloption']")
        Nextbutton_two = driver.find_element(By.XPATH, "//input[@class='NextButton']")
        ActionChains(driver)\
            .click(Highlysatisfieds[0])\
            .click(Highlysatisfieds[1])\
            .click(Highlysatisfieds[2])\
            .click(Highlysatisfieds[3])\
            .click(Highlysatisfieds[4])\
            .click(Highlysatisfieds[5])\
            .click(Nextbutton_two)\
            .perform()
        time.sleep(1)
        Dumbbutton = driver.find_element(By.XPATH, "//td[@class='Opt2 inputtyperbloption']")
        Nextbutton_three = driver.find_element(By.XPATH, "//input[@class='NextButton']")
        ActionChains(driver)\
            .click(Dumbbutton)\
            .click(Nextbutton_three)\
            .perform()
        time.sleep(1)
        # No_problem = driver.find_element(By.XPATH, "//td[@class='Opt2 inputtyperbloption']")
        # Nextbutton_four = driver.find_element(By.XPATH, "//input[@class='NextButton']")
        # ActionChains(driver)\
        #     .click(No_problem)\
        #     .click(Nextbutton_four)\
        #     .perform()
        # time.sleep(1)
        textarea = driver.find_element(By.XPATH, "//textarea[@name='S081000']")
        Nextbutton_five = driver.find_element(By.XPATH, "//input[@class='NextButton']")
        ravingreview = "Breakfast burrito\nEpic Service\nSupreme burrito\nTime for taco\n\nTaco\nAbsolutely\nCracked\nOkay?\n\nBurrito is my\nEternal\nLove\nLanguage"
        ActionChains(driver)\
            .send_keys_to_element(textarea, ravingreview)\
            .click(Nextbutton_five)\
            .perform()
        time.sleep(1)
        yes = driver.find_element(By.XPATH, "//td[@class='Opt1 inputtyperbloption']")
        Nextbutton_six = driver.find_element(By.XPATH, "//input[@class='NextButton']")
        ActionChains(driver)\
            .click(yes)\
            .click(Nextbutton_six)\
            .perform()
        time.sleep(1)
        textfield_one = driver.find_element(By.ID, "S081001")
        textfield_two = driver.find_element(By.ID, "S081002")
        employee_name = 'kayla'
        employee_epic = 'breakfast at 10:48 crazy'
        Nextbutton_seven = driver.find_element(By.XPATH, "//input[@class='NextButton']")
        ActionChains(driver)\
            .send_keys_to_element(textfield_one, employee_name)\
            .send_keys_to_element(textfield_two, employee_epic)\
            .click(Nextbutton_seven)\
            .perform()
        time.sleep(1)
        no_button = driver.find_element(By.XPATH, "//td[@class='Opt2 inputtyperbloption']")
        Nextbutton_eight = driver.find_element(By.XPATH, "//input[@class='NextButton']")
        ActionChains(driver)\
            .click(no_button)\
            .click(Nextbutton_eight)\
            .perform()
        time.sleep(2)
        yes_button = driver.find_element(By.XPATH, "//td[@class='Opt1 inputtyperbloption']")
        Nextbutton_nine = driver.find_element(By.XPATH, "//input[@class='NextButton']")
        ActionChains(driver)\
            .click(yes_button)\
            .click(Nextbutton_nine)\
            .perform()
        time.sleep(1)
        firstname_field = driver.find_element(By.XPATH, "//input[@name='S090100']")
        lastname_field = driver.find_element(By.XPATH, "//input[@name='S090200']")
        number_field = driver.find_element(By.XPATH, "//input[@name='S092000']")
        Nextbutton_ten = driver.find_element(By.XPATH, "//input[@class='NextButton']")
        firstname = 'Jaxton'
        lastname = 'Gettling'
        number = '4176992857'
        ActionChains(driver)\
            .send_keys_to_element(firstname_field, firstname)\
            .send_keys_to_element(lastname_field, lastname)\
            .send_keys_to_element(number_field, number)\
            .click(Nextbutton_ten)\
            .perform()
        time.sleep(2)
        driver.quit()
    except NoSuchElementException:
        openSurvey()

while True:
    openSurvey()
