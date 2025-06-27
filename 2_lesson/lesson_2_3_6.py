from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    first_window = browser.window_handles[0] # запоминаем вкладку, в которой находимся


    # нажимаем кнопку
    button1 = browser.find_element(By.XPATH, "//button[contains(@class, 'trollface')]")
    button1.click()

    # запоминаем новую вкладку и переходим к ней
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # находим x, сохраняем значение в y
    x_element = browser.find_element(By.XPATH, "//label/span[@id='input_value']")
    x = x_element.text
    y = calc(x)

    # вставляем значение в инпут
    input1 = browser.find_element(By.XPATH, "//input[@id='answer']")
    input1.send_keys(y)

    # нажимаем на кнопку для отправки значения
    button2 = browser.find_element(By.XPATH, "//button[@type='submit']")
    button2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла