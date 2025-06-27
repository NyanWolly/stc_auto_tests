from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/wait1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    time.sleep(1)
    # нажимаем кнопку
    button = browser.find_element(By.XPATH, "//button[contains(@id, 'verify')]")
    button.click()

    message = browser.find_element(By.XPATH, "//div[contains(@id, 'verify_message')]")
    assert "successful" in message.text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла