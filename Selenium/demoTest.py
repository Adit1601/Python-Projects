import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# using manually downloaded chromedriver, edgedriver, geckodriver
# Service = Service("../chromedriver-win64/chromedriver.exe")
# driver = webdriver.Chrome(service=Service)


# Auto fetch of chrome driver based on chrome version installed in the system
driver = webdriver.Edge()
driver.get("https://www.google.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)


time.sleep(2)
driver.close()
