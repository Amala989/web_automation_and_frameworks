from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox()
driver.maximize_window()

url = "https://demo.automationtesting.in/Datepicker.html"
driver.get(url)

actions = ActionChains(driver)

# Locate the element first before clicking
hover_element = driver.find_element(By.XPATH, "//a[normalize-space()='SwitchTo']")
actions.move_to_element(hover_element).perform()
time.sleep(2)

# Now click on the "Frames" link under the hovered menu
driver.find_element(By.XPATH, "//a[normalize-space()='Frames']").click()
time.sleep(3)
