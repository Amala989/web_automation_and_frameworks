from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox()
driver.maximize_window()
url = "https://the-internet.herokuapp.com/horizontal_slider"
driver.get(url)
slider = driver.find_element(By.XPATH, "//input[@type='range']")
actions = ActionChains(driver)
actions.click_and_hold(slider).move_by_offset(25,0).release().perform()
time.sleep(5)
driver.quit()