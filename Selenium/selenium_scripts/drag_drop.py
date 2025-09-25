from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox()
driver.maximize_window()
url = "https://the-internet.herokuapp.com/drag_and_drop"
driver.get(url)
source_element = driver.find_element(By.ID, "column-a")
destination_element = driver.find_element(By.ID,"column-b")
actions = ActionChains(driver)
actions.drag_and_drop(source_element,destination_element).perform()
time.sleep(5)
driver.quit()