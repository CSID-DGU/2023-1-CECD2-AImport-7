from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get("http://bugeyedmonkeys.com/lic/")

version_check = browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div[3]/span')
version_check.click()

language_select = browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div[3]/span')
language_select.click()

open_ldr = browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div/ul/li[1]/a')
open_ldr.click()

time.sleep(1000)
