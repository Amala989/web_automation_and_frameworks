from selenium import webdriver
from selenium.webdriver.common.by import By 
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.get('https://the-internet.herokuapp.com/iframe')

iframe = driver.find_element(By.ID, "mce_0_ifr")
driver.switch_to.frame(iframe)

Text_Editor = driver.find_element(By.ID, "tinymce")
Text_Editor.clear()
Text_Editor.send_keys("This is selenium with python iframe concept.")
time.sleep(3)

driver.switch_to.default_content()
link = driver.find_element(By.XPATH, "//a[normalize-space()='Elemental Selenium']")
link.click()