import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
# print(driver.title)
# print(driver.current_url)
driver.find_element(By.XPATH,"//*[@placeholder='Type to Select Countries']").send_keys("Ind")
time.sleep(1)
countries = driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']/div")

# All the below implementations are under assumption that, dropdowns options,
# checkbox options and radio button options are changing dynamically

for country in countries:
    if country.text == "India":
        country.click()
        break
# Get attribute when element is not present in DOM and text does not work
assert driver.find_element(By.ID,"autocomplete").get_attribute('value') == "India"

# it works but not satisfactory as looking at the code it do not suggests much. Refer next implementation
optionsList = driver.find_elements(By.XPATH,"//*[text()='Checkbox Example']/following-sibling::label")
for option in optionsList:
    if option.text.strip() == "Option2":
        # getting locators of element inside the element
        option.find_element(By.TAG_NAME,"input").click()
        assert option.find_element(By.TAG_NAME, "input").is_selected()
        break

# This only works when value attribute is there
radioButtons = driver.find_elements(By.XPATH, "//*[@type='radio']")
for radioButton in radioButtons:
    if radioButton.get_attribute("value") == "radio3":
        radioButton.click()
        assert radioButton.is_selected()
        break

# id_displayed method
assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()

name = "Adit"
driver.find_element(By.ID, "name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()
alertObj = driver.switch_to.alert
assert name in alertObj.text
# accept alert
alertObj.accept()
# dismiss alert
# alertObj.dismiss()

driver.find_element(By.ID, "opentab").click()

handles = driver.window_handles
for handle in handles:
    driver.switch_to.window(handle)
    if "QAClick Academy" in driver.title:
        print(driver.current_url)
        break

time.sleep(2)

driver.close()
driver.quit()