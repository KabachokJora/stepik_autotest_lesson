from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from math import *
import time

browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 18).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    button2 = browser.find_element_by_id("book")
    button2.click()


    field = browser.find_element_by_tag_name("label")
    browser.execute_script("return arguments[0].scrollIntoView(true);", field)

    x = browser.find_element_by_id('input_value').text
    browser.find_element_by_id("answer").send_keys(str(log(abs(12*sin(int(x))))))

    browser.find_element_by_id("solve").click()
    alert = browser.switch_to.alert
    print(alert.text)


finally:
    browser.execute_script("alert('Все обосралось')")
    time.sleep(5)
    browser.quit()