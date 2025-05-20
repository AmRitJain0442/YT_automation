from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service=Service(executable_path="C:\Program Files (x86)\chromedriver.exe")
driver =webdriver.Chrome(service=service)
driver.get("https://www.youtube.com/@funniestanimalsever7995/videos")

WebDriverWait(driver,5).until(
    EC.presence_of_all_elements_located((By.XPATH,"//yt-formatted-string[@aria-label]"))
)
input_element= driver.find_elements(By.XPATH,"//yt-formatted-string[@aria-label]")
input_element.clear()

link= driver.find_elements(By.XPATH,"//yt-formatted-string[@aria-label]")
print(link)

