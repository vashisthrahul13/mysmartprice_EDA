from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
import json

service = Service("chromedriver-mac-arm64/chromedriver")
chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
chrome_options.add_argument("--disable-notifications")  # Blocks popups
chrome_options.add_argument("--disable-infobars")  # Blocks the Chrome "Chrome is being controlled" banner

driver = webdriver.Chrome(service= service , options= chrome_options)

driver.get("https://www.mysmartprice.com/mobile/pricelist/mobile-price-list-in-india.html")
time.sleep(2)
print(len(driver.find_elements(By.XPATH, "//*[contains(@class, 'spec_card')]")))

page_no = 1
flag=0

while flag==0:
    
    print("page_height : " , driver.execute_script('return document.body.scrollHeight'))
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    time.sleep(2)


    try:
        load_more = driver.find_element(By.XPATH, "//*[contains(@class, 'w-f-100 txt-c load_more prdct-list__more-wrpr')]")
        load_more.click()
        time.sleep(5)

        elements = driver.find_elements(By.XPATH, "//*[contains(@class, 'spec_card')]")
        print(len(elements))

    except:
        flag=1
    
    print(page_no)
    page_no+=1
    
    # if page_no>=5:
    #     break

html = driver.page_source

with open('mysmartprice.html' , 'w' , encoding= 'utf-8') as f:
    f.write(html)