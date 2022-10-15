from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get(url='https://www.signal.bz/')
time.sleep(5)

ranktime = driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div/section/div/section/section[1]/div[1]/div[1]/span').text
print(ranktime)
ranks = driver.find_elements(By.CLASS_NAME, 'rank-layer')

for rank in ranks:
    num = rank.find_element(By.CLASS_NAME, 'rank-num').text
    search = rank.find_element(By.CLASS_NAME, 'rank-text').text
    print(num + '. ' + search)