from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/wait1.html"
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)
    
    button1 = browser.find_element(By.CSS_SELECTOR, "#verify")
    button1.click()
    
    message = browser.find_element(By.CSS_SELECTOR, "#verify_message")
    
    assert "successful" in message.text
    
    
finally:
    time.sleep(10)
    browser.quit()
