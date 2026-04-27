from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

driver = webdriver.Chrome()
file_path = "file://" + os.path.abspath("index.html")
driver.get(file_path)

try:
    # Fill form
    driver.find_element(By.ID, "name").send_keys("DevOps Admin")
    driver.find_element(By.ID, "email").send_keys("admin@devops.com")
    time.sleep(1) # Visual delay for the lab

    # Click Submit
    driver.find_element(By.ID, "submitBtn").click()
    
    # Wait for JS to update the status
    time.sleep(1) 

    # Verify result
    status_text = driver.find_element(By.ID, "status").text
    print(f"Current Status: {status_text}")

    if "Success!" in status_text:
        print("✓ SELENIUM TEST PASSED!")
    else:
        print("X TEST FAILED: Status message not found.")

except Exception as e:
    print(f"Error: {e}")

time.sleep(2)
driver.quit()
