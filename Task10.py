from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
driver = webdriver.Chrome()
driver.get("https://www.instagram.com/guviofficial/")
time.sleep(5)
print(driver.current_url)
#####USING RELATIVE XPATH#######
followers_text=driver.find_element(By.XPATH,"//*[contains(text(),' followers')]").text
time.sleep(5)
print(followers_text)
following_text=driver.find_element(By.XPATH,"//*[contains(text(),' following')]").text
time.sleep(5)
print(following_text)


