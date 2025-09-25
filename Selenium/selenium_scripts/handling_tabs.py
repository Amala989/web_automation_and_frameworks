from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.get('https://www.selenium.dev/')
driver.switch_to.new_window()
driver.get('https://amazon.com/')

# Number of tabs
num_tabs = len(driver.window_handles)
print(f"Number if tabs {num_tabs}")

# unique value of tab
tabs_value = driver.window_handles
print(f"Tab value {tabs_value}")

# value of current tab
current_tab = driver.current_window_handle
print(f"current window tab {current_tab}")