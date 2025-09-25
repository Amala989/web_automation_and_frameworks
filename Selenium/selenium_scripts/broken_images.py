from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

driver = webdriver.Firefox()
driver.maximize_window()
driver.get('https://the-internet.herokuapp.com/broken_images')
images = driver.find_elements(By.TAG_NAME, 'img')
broken_images = []

for img in images:
    src = img.get_attribute("src")
    if src:
        response = requests.get(src)
        if response.status_code != 200:
            broken_images.append(src)
            print(f"Broken image found")

if broken_images:
    print(f"List of broken images:")
    for imge in broken_images:
        print(imge)
else:
    print("No broken images found.")