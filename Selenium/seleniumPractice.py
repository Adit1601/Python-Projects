import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
# If element is not visible then it will wait for maximum 5 secs before throwing exception.
# if element is visible in 3 seconds then it will proceed forward.
# this implecit wait do not work for find_elements method. If locator not found, then it would return
# an empty list. And empty list is still a valid list. Selenium will not check if list is not empty or not.
# Implicit is declared globally and applies to whole page.
driver.implicitly_wait(1)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.XPATH,"//input[@type='search']").send_keys("ber")
driver.find_element(By.XPATH,"//*[@type='submit']").click()
time.sleep(1)
results = driver.find_elements(By.XPATH, "//*[@class='products']/div")
assert len(results)>0

addedItems = []
for result in results:
    addedItems.append(result.find_element(By.XPATH, "h4").text)
    result.find_element(By.XPATH, "//*[text()='ADD TO CART']").click()

cart_details = driver.find_elements(By.XPATH, "//*[@class='cart-info']/table/tbody/tr")
for cart_detail in cart_details:
    if "Items" in cart_detail.find_element(By.XPATH, "td[1]").text:
        assert int(cart_detail.find_element(By.XPATH, "td[3]/strong").text) == len(results)

driver.find_element(By.XPATH, "//a[@class='cart-icon']").click()
cart_preview_items = driver.find_elements(By.XPATH, "//*[@class='cart-preview active']/descendant::*[@class='product-name']")
for item in cart_preview_items:
    assert item.text in addedItems
driver.find_element(By.XPATH, "//*[text()='PROCEED TO CHECKOUT']").click()
cart_data = driver.find_elements(By.XPATH, "//tbody/descendant::tr/td[5]/p")
sum=0
for data in cart_data:
   sum+=int(data.text)
assert sum == int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
# Explicit wait overwrites the implicit waits.
# explicit wait by name suggests that wait gets explicitly applied to particular element. and not
# whole page.
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"promoInfo")))
assert "Code applied" in driver.find_element(By.CLASS_NAME, "promoInfo").text
driver.close()