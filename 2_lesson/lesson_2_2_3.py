from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

link = "https://suninjuly.github.io/selects1.html"
link2 = "http://suninjuly.github.io/selects2.html"

def calc(a, b):
    return str(int(a) + int(b))

try:
    browser = webdriver.Chrome()
    browser.get(link2)

    #проверяем значение атрибута 1
    attribute = browser.find_element(By.ID, "num1")
    attribute2 = browser.find_element(By.ID, "num2")
    a = attribute.text
    b = attribute2.text
    value = calc(a, b)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(value)  # ищем элемент

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла