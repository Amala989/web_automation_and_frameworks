from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.maximize_window()
url = "https://the-internet.herokuapp.com/javascript_alerts"
driver.get(url)

# Accepting first one
alert_button = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Alert']")
alert_button.click()
alert = driver.switch_to.alert
alert_text = alert.text
print(f"alert text is {alert_text}")
time.sleep(2)
alert.accept()
time.sleep(3)

# Accepting second one
alert_button_2 = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Confirm']")
alert_button_2.click()
alert2 = driver.switch_to.alert
alert_text2 = alert.text
print("Alert2 text is", alert_text2)
time.sleep(2)
# Accept alert
# alert2.accept()

# Dismiss alert
alert2.dismiss()
time.sleep(2)

# Input alert
input_alert_button = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']")
input_alert_button.click()
input_alert = driver.switch_to.alert
input_alert_text = input_alert.text
print(f"Input alert text is : {input_alert_text}")
time.sleep(3)
input_alert.send_keys("This is selenium with python javascript alerts concept")
input_alert.accept()
time.sleep(3)