from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestFindSelectors(unittest.TestCase):

    def test_find_selectors1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.XPATH, "//div[@class='first_block']//input[@class='form-control first']")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, "//div[@class='first_block']//input[@class='form-control second']")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH, "//div[@class='first_block']//input[@class='form-control third']")
        input3.send_keys("111@mail.ru")


        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        exactly = "Congratulations! You have successfully registered!"
        self.assertEqual(exactly, welcome_text, f"Текстовка различается. ОР: {exactly}, ФР: {welcome_text}")

    #     # ожидание чтобы визуально оценить результаты прохождения скрипта
    #     time.sleep(10)
    #     # закрываем браузер после всех манипуляций
        browser.quit()
    #
    # # не забываем оставить пустую строку в конце файла

    def test_find_selectors2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.XPATH, "//div[@class='first_block']//input[@class='form-control first']")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, "//div[@class='first_block']//input[@class='form-control second']")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH, "//div[@class='first_block']//input[@class='form-control third']")
        input3.send_keys("111@mail.ru")


        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        exactly = "Congratulations! You have successfully registered!"
        self.assertEqual(exactly, welcome_text, f"Текстовка различается. ОР: {exactly}, ФР: {welcome_text}")

    #     # ожидание чтобы визуально оценить результаты прохождения скрипта
    #     time.sleep(10)
    #     # закрываем браузер после всех манипуляций
        browser.quit()
    #
    # # не забываем оставить пустую строку в конце файла

if __name__ == "__main__":
    unittest.main()