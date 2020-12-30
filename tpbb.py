from selenium import webdriver
from selenium.webdriver.common.by import By
import time

path = "C:\Program Files (x86)\Google\Chrome\chromedriver.exe"
driver = webdriver.Chrome(path)
driver1=webdriver.Chrome(path)

while True:
    try:
        driver.get("https://www.target.com/p/playstation-5-console/-/A-81114595#lnk=sametab")
        driver1.get("https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149")
        finder = driver.find_element_by_class_name("l-container-fixed")
        ss = finder.find_elements(By.TAG_NAME, 'div')
        li = ss[4].find_elements(By.TAG_NAME, 'div')
        time.sleep(3)
        status = ['', '']
        status[0] = li[145].text[:31]
        status[1] = li[145].text[32:62]
        t=status[0]
        t1=status[1]
        print('Target: ' + status[0])
        print('Target: ' + status[1])
        status1=driver1.find_element_by_class_name("fulfillment-add-to-cart-button").text
        print("BestBuy: " +status1)
        if not status or status[0] != t or status[1] != t1:
            print('In Stock')
            break
        if not status1 or status1!='Sold Out':
            print('In Stock')
            break
        driver.refresh()
        driver1.refresh()
        time.sleep(10)
    except:
        print('Bot Trace')
        driver.quit()
        driver1.quit()
        break
