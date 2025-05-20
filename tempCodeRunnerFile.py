WebDriverWait(driver,15).until(
    EC.presence_of_element_located((By.XPATH,'/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[3]/div'))
)

save_but=driver.find_element(By.XPATH,'/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[3]/div')
save_but.click()