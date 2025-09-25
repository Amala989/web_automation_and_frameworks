from selenium import webdriver
import time

viewports = [(1024,768),(768,1024),(375,667),(414,896)]
driver = webdriver.Firefox()
driver.get('https://www.gooogle.com/')
# driver.set_window_size(768,1024)
time.sleep(3)

try:
    for width,height in viewports:
        driver.set_window_size(width,height)
        time.sleep(3)
finally:
    driver.close()