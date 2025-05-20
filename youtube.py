from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.service import Service

email = "bitsburiburi@gmail.com"
password = "buriburi123"

service=Service(executable_path="C:\Program Files (x86)\chromedriver.exe")
driver =webdriver.Chrome(service=service)

try:
    # Open YouTube
    driver.get("https://www.youtube.com")

    # Click on the sign in button
    sign_in_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//yt-formatted-string[text()='Sign in']"))
    )
    sign_in_button.click()

    # Enter email
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='email']"))
    )
    email_field.send_keys(email)
    email_field.send_keys(Keys.ENTER)

    # Wait for the password field to appear and enter the password
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='password']"))
    )
    password_field.send_keys(password)
    password_field.send_keys(Keys.ENTER)

    # Handle potential two-step verification (if any)
    # Add necessary steps here if your account has two-step verification enabled

    # Wait for a while to ensure login is complete
    time.sleep(5)

    # Verify login
    if "account" in driver.current_url:
        print("Logged in successfully")
    else:
        print("Login failed")

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the driver
    driver.quit()
