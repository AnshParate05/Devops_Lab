from selenium import webdriver
import os
import time

# Setup the browser
driver = webdriver.Chrome()

# Open your local file
file_path = "file://" + os.path.abspath("index.html")
driver.get(file_path)

# Verify the title
if "My Web App" in driver.title:
    print("✓ SUCCESS: Website loaded with correct title.")
else:
    print("X FAILED: Title does not match.")

# Wait 3 seconds so you can see it, then close
time.sleep(3)
driver.quit()
