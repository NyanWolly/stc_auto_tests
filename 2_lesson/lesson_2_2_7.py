from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
print(current_dir)
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
print(file_path)
#element.send_keys(file_path)