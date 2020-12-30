from selenium import webdriver
from selenium.webdriver.common.by import By
import time
path = "C:\Program Files (x86)\Google\Chrome\chromedriver.exe"
driver = webdriver.Chrome(path)
while True:
    try:
        driver.get("https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149")
        status=driver.find_element_by_class_name("fulfillment-add-to-cart-button").text
        print("BestBuy: " +status)
        if not status or status!='Sold Out':
            print('In Stock')
            break
        driver.refresh()
        time.sleep(5)
    except:
        print('Bot Trace')
        driver.quit()
        break