from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
# https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
driver.get('https://opensource-demo.orangehrmlive.com/')
driver.fullscreen_window()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,".oxd-text.oxd-text--p.orangehrm-login-forgot-header")
time.sleep(5)
driver.back()
time.sleep(5)
driver.forward()
time.sleep(5)
driver.refresh()
time.sleep(2)
driver.close()