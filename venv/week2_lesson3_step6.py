from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

def buttton():
    button = browser.find_element_by_css_selector("button")
    button.click()

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    buttton()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    #alert = browser.switch_to.alert
    #alert.accept()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_css_selector('[class="form-control"]')
    input1.send_keys(y)

    buttton()

finally:
    time.sleep(5)
    browser.quit()