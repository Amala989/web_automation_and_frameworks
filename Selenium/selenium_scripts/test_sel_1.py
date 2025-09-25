from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get('https://selenium.dev/')
driver.maximize_window()
title = driver.title
print(title)
# time.sleep(5)
# driver.quit()
assert "Selenium" in title