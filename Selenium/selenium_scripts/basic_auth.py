from selenium import webdriver
from selenium.webdriver.common.by import By
import time

username = "admin"
password = "admin"
driver = webdriver.Firefox()
driver.maximize_window()
url = "https://admin:admin@the-internet.herokuapp.com/basic_auth"
# syntax: "https://username:password@damain/path" 
driver.get(url)
time.sleep(5)