from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
path = "C:\Program Files (x86)\Google\Chrome\chromedriver.exe"
driver = webdriver.Chrome(path)
while True:
    try:
        driver.get("https://www.walmart.com/ip/PlayStation-5-Console/363472942")
        a=driver.find_element_by_class_name("prod-PriceSection")
        b=a.find_elements(By.CLASS_NAME,'Grid-col')
        status=b[-1].find_element_by_tag_name('span').text
        print('Walmart: '+ status)
        if not status or status!='Out of stock':
            print('In Stock')
            break
        driver.refresh()
        time.sleep(8)
    except:
        print('Bot Trace')
        time.sleep(80)


 