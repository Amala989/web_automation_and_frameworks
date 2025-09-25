from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get('https://contactform7.com/checkboxes-radio-buttons-and-menus/')
driver.maximize_window()
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # to scrolldown, (javascript code)
time.sleep(3)
# driver.find_element(By.XPATH, "//input[@value='India']").click()
# time.sleep(5)
# driver.find_element(By.XPATH, "//input[@value='India']").click()
# time.sleep(3)
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
for checkbox in checkboxes:
    # checkbox.send_keys(Keys.SPACE)
    driver.execute_script("arguments[0].scrollIntoView();", checkbox)
    checkbox.click()
    time.sleep(1)
check_count = 0
for checkbox in checkboxes:
    if checkbox.is_selected():
        check_count+=1
print("checkbox_count = ",check_count)
expected_check_count = 4
if check_count == expected_check_count:
    print('Checkbox count verified.')
else:
    print("Checkbox_count mismatch")
time.sleep(2)
driver.close()
    


    