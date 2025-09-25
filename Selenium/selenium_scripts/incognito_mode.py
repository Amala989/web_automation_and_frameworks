from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

firefox_options = Options()
firefox_options.add_argument("--private")

driver = webdriver.Firefox(options=firefox_options)
driver.maximize_window()
time.sleep(5)
driver.get("https://www.google.com/")