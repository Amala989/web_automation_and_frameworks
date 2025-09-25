from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

driver = webdriver.Firefox()
driver.maximize_window()
url = "https://jqueryui.com/"
driver.get(url)

all_links = driver.find_elements(By.TAG_NAME, 'a')
print(f"Total number of link on the page: {len(all_links)}")

for link in all_links:
    href = link.get_attribute('href')
    response = requests.get(href)
    if response.status_code>=400:
        print(f"Link Broken : {href}(status code: {response.status_code})")
driver.quit()