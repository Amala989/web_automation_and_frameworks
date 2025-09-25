from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.get('https://the-internet.herokuapp.com/nested_frames')

# Switching to top frmae
driver.switch_to.frame("frame-top")

# Switching to middle frame
driver.switch_to.frame("frame-middle")

content = driver.find_element(By.ID, "content").text
print(f"The content in middle frame {content}")

# Switching to bottom frame
driver.switch_to.default_content()
driver.switch_to.frame("frame-bottom")
content_bottom = driver.find_element(By.TAG_NAME,"body").text
print(f"Bottom frame content: {content_bottom}")