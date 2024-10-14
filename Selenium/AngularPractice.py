import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

# ID, XPath, ClassName, Name, Text, CSSSelectors, LinkText
# Handle form fill
driver.find_element(By.NAME,"name").send_keys("Adit")
driver.find_element(By.NAME,"email").send_keys("adit@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("password")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("AditHelloAgain")

# Handle checkbox
driver.find_element(By.XPATH,"//*[@type='checkbox']").click()
driver.find_element(By.XPATH, "//select[@id='exampleFormControlSelect1']")
# Handle Radio Button
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
# Handle Static Dropdown
# Select by index(starts with 0), visible Text, and value (works only when option attribute is present).
# Check for select tag, and then use Select class method.
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)

driver.find_element(By.XPATH, "//*[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()

time.sleep(5)
driver.close()
driver.quit()