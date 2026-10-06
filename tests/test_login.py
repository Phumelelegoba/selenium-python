from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://testing.co.za")

username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
username_field.send_keys("Phumelele")

driver.find_element(By.XPATH, "//button[@title='Sign in']").click()

password_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "password")))
password_field.send_keys("Goba", Keys.ENTER)

WebDriverWait(driver, 10).until(EC.url_contains("landing"))

import time
time.sleep(5)  # stays open for 10 seconds before closing

print("Login successful!")

driver.quit()

