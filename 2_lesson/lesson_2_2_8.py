from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"



try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.XPATH, "//div[@class='form-group']/input[@name='firstname']")
    first_name.send_keys("John")

    last_name = browser.find_element(By.XPATH, "//div[@class='form-group']/input[@name='lastname']")
    last_name.send_keys("Smith")

    email_name = browser.find_element(By.XPATH, "//div[@class='form-group']/input[@name='email']")
    email_name.send_keys("js@mail.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    print(current_dir)
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    print(file_path)
    element = browser.find_element(By.XPATH, "//input[@id='file']")
    element.send_keys(file_path)

    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла