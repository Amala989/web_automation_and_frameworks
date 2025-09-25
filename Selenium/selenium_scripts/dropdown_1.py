from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
login_url = "https://the-internet.herokuapp.com/dropdown"
driver.get(login_url)

dropdown_element = driver.find_element(By.ID, "dropdown")
select = Select(dropdown_element)

# selct the value by visisble text.
# select.select_by_visible_text("Option 2")

# selct the value by index
# select.select_by_index(1)

# select the option by using a value
# select.select_by_value("1")

# count the dropdown values.
option_count = len(select.options)
expected_count = 3
if option_count == expected_count:
    print("Testcase passed, count is correct")
else:
    print("Testcase failed, Count is incorrect")

# Select only if desired option is there else ignore.
target_value = "Option 3"
for option in select.options:
    if option.text == target_value:
        option.click()
        print(f"Selected option is {target_value}")
        break
    else:
        print(f"{target_value} not found in dropdown")
        
