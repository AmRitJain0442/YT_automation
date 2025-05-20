from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service=Service(executable_path="C:\Program Files (x86)\chromedriver.exe")
driver =webdriver.Chrome(service=service)
driver.get("https://google.com")

WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.CLASS_NAME,"gLFyf"))
)

input_element= driver.find_element(By.CLASS_NAME,"gLFyf")
input_element.clear()
input_element.send_keys("bits pilani"+ Keys.ENTER)

link = driver.find_element(By.PARTIAL_LINK_TEXT,"Birla Institute of Technology And Science, Pilani (BITS Pilani)")
link.click()
time.sleep(10)

driver.quit()