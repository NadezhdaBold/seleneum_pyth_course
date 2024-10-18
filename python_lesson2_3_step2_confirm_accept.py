from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

link = "https://suninjuly.github.io/alert_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button1.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    time.sleep(2)

    span1 = browser.find_element(By.XPATH, '//span[@id="input_value"]')
    x = span1.text
    y = calc(x)

    input1 = browser.find_element(By.XPATH, '//input[@id="answer"]')
    input1.send_keys(y)

    button2 = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button2.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()