from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.XPATH, "//h5[contains(@id, 'price')]"), "100")
        )
    button = browser.find_element(By.XPATH, "//button[contains(@id, 'book')]")
    button.click()

    x_element = browser.find_element(By.XPATH, "//span[contains(@id, 'input_value')]")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.XPATH, "//input[contains(@id, 'answer')]")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
    input1.send_keys(y)

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@id, 'solve')]"))
    )
    button.click()

    # # говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной
    # button = WebDriverWait(browser, 5).until_not(
    #         EC.element_to_be_clickable((By.XPATH, "//button[contains(@id, 'solve')]"))
    #     )


finally:
    time.sleep(10)

    browser.quit()

