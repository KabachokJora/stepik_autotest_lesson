from selenium import webdriver
import time
from math import *


browser = webdriver.Chrome()


try:
    browser.get('http://suninjuly.github.io/alert_accept.html')
    browser.find_element_by_class_name('btn.btn-primary').click()
    browser.switch_to.alert.accept()
    x = browser.find_element_by_id('input_value').text
    browser.find_element_by_id('answer').send_keys(str(log(abs(12*sin(int(x))))))
    browser.find_element_by_class_name('btn.btn-primary').click()


finally:
    time.sleep(3)
    browser.quit()