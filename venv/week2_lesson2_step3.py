from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_find = browser.find_element_by_id("num1")
    y_find = browser.find_element_by_id("num2")
    x = int(x_find.text)
    y = int(y_find.text)
    z = x + y

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(z))

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()