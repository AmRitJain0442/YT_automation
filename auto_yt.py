from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service=Service(executable_path="C:\Program Files (x86)\chromedriver.exe")
driver =webdriver.Chrome(service=service)


email = "bitsburiburi@gmail.com"
password = ""

description="Get ready for a MEGA dose of adorableness! This short compilation is packed with the cutest moments between our furry feline and canine friends. You'll see playful pups, cuddly kitties, and the most heartwarming friendships that will melt your heart." 

count=1
LOOP=0

while count!=0:
    driver.get("https://www.youtube.com")
    WebDriverWait(driver,10).until(
        EC.presence_of_all_elements_located((By.XPATH,'//*[@id="buttons"]/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]'))
    )

    sign_up=driver.find_element(By.XPATH,'//*[@id="buttons"]/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]')
    sign_up.click()

    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="identifierId"]'))
    )
    email_field.send_keys(email)
    email_field.send_keys(Keys.ENTER)

    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="password"]/div[1]/div/div[1]/input'))
    )
    password_field.send_keys(password)
    password_field.send_keys(Keys.ENTER)

    WebDriverWait(driver,15).until(
        EC.presence_of_element_located((By.XPATH,'/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[3]/div[2]/ytd-topbar-menu-button-renderer[1]/div/a/yt-icon-button/button/yt-icon/yt-icon-shape/icon-shape/div'))
    )

    upload_but=driver.find_element(By.XPATH,'/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[3]/div[2]/ytd-topbar-menu-button-renderer[1]/div/a/yt-icon-button/button/yt-icon/yt-icon-shape/icon-shape/div')
    upload_but.click()

    WebDriverWait(driver,15).until(
        EC.presence_of_element_located((By.XPATH,'/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer/div[2]/ytd-compact-link-renderer[1]/a/tp-yt-paper-item/div[2]/yt-formatted-string[1]'))
    )

    upload_but2=driver.find_element(By.XPATH,'/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer/div[2]/ytd-compact-link-renderer[1]/a/tp-yt-paper-item/div[2]/yt-formatted-string[1]')
    upload_but2.click()

    WebDriverWait(driver,15).until(
        EC.presence_of_element_located((By.XPATH,'/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-uploads-file-picker/div/ytcp-button/div'))
    )

    sel_but=driver.find_element(By.XPATH,'/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-uploads-file-picker/div/ytcp-button/div')
    sel_but.click()

    file_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//input[@type="file"]'))
    )
    file_input.send_keys(r'C:\Users\amrit\OneDrive\Desktop\yt_videos\vid_01.mp4')

    disc_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[2]/ytcp-video-description/div/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-social-suggestion-input/div'))
    )
    disc_input.send_keys(description)

    WebDriverWait(driver,15).until(
        EC.presence_of_element_located((By.XPATH,'/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[5]/ytkc-made-for-kids-select/div[4]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[2]/div[1]/div[1]'))
    )

    not_for_kids=driver.find_element(By.XPATH,'/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[5]/ytkc-made-for-kids-select/div[4]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[2]/div[1]/div[1]')
    not_for_kids.click()

    for _ in range(3):
        WebDriverWait(driver,15).until(
            EC.presence_of_element_located((By.XPATH,'/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[2]/div'))
        )

        next_but=driver.find_element(By.XPATH,'/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[2]/div')
        next_but.click()


    WebDriverWait(driver,15).until(
        EC.presence_of_element_located((By.XPATH,'/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-review/div[2]/div[1]/ytcp-video-visibility-select/div[2]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[3]/div[1]/div[1]'))
    )

    pub=driver.find_element(By.XPATH,'/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-review/div[2]/div[1]/ytcp-video-visibility-select/div[2]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[3]/div[1]/div[1]')
    pub.click()

    time.sleep(5)

    WebDriverWait(driver,15).until(
        EC.presence_of_element_located((By.XPATH,'/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[3]/div'))
    )

    save_but=driver.find_element(By.XPATH,'/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[3]/div')
    save_but.click()

    time.sleep(900)
    driver.close()
    LOOP+=1
    print(f"Video {LOOP} Uploaded SUCCESFULLY")
    print("Working on the next one.........")
    count-=1

