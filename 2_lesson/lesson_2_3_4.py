from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element(By.XPATH, "//button[@type='submit']")
    button1.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element(By.XPATH, "//label/span[@id='input_value']")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.XPATH, "//input[@id='answer']")
    input1.send_keys(y)

    button2 = browser.find_element(By.XPATH, "//button[@type='submit']")
    button2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла