from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime,timedelta
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.maximize_window()
url = "https://demo.automationtesting.in/Datepicker.html"
driver.get(url)
date_picker_button = driver.find_element(By.ID, "datepicker2")
date_picker_button.click()
time.sleep(3)
current_date = datetime.now()
print(current_date)
next_date = current_date+timedelta(days=1)
print(next_date)
next_day = str(next_date.day)
print(next_day)
current_month = datetime.now().month
current_year = datetime.now().year

next_month = (current_month % 12)+1
next_year = f"{next_month}/{current_year}"

month_dropdown = driver.find_element(By.CSS_SELECTOR, "select[title='Change the month']")
select = Select(month_dropdown)
select.select_by_value(str(next_year))
time.sleep(1)
year_dropdown = driver.find_element(By.CSS_SELECTOR, "select[title='Change the year']")
select = Select(year_dropdown)
select.select_by_visible_text("2025")
driver.find_element(By.LINK_TEXT, next_day).click()
time.sleep(3)