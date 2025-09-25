from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox()
driver.maximize_window()
url = "https://demo.automationtesting.in/Resizable.html"
driver.get(url)
resizable_element = driver.find_element(By.XPATH, "//div[@class='ui-resizable-handle ui-resizable-e']")
intial_element_size = driver.find_element(By.XPATH,"//div[@id='resizable']")
initial_size = intial_element_size.size
print(f"initial size: {initial_size}")
time.sleep(5)
action_chains = ActionChains(driver)
action_chains.click_and_hold(resizable_element).move_by_offset(100,200).release().perform()
time.sleep(5)
resized_element = intial_element_size.size
print(f"resized element size {resized_element}")
driver.quit()