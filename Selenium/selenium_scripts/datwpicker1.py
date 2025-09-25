from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time
from datetime import datetime, timedelta

driver = webdriver.Firefox()
driver.maximize_window()
url = "https://www.globalsqa.com/demo-site/datepicker/"
driver.get(url)

driver.find_element(By.XPATH, "//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//div[@class='attention closable'][normalize-space()='Pick a date by clicking on the text box.']")
frame = driver.find_element(By.XPATH, "//iframe[contains(@class, 'demo-frame')]")
driver.switch_to.frame(frame)
time.sleep(3)
date_picker = driver.find_element(By.CSS_SELECTOR, "#datepicker")
date_picker.click()
# current_date = datetime.now()
# next_date = current_date + timedelta(days=1)
mrg_date = datetime(2025,2,15)
formatted_date = mrg_date.strftime("%d/%m/%y")
date_picker.send_keys(formatted_date + Keys.TAB)
time.sleep(3)
driver.quit()