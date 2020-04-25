from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import privateurl
import time
url = privateurl.wilson_url

browser = webdriver.Safari()

browser.get(url)

timeout = 20
try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.ID, "button_correct")))
except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()

button_correct = browser.find_element_by_id("button_correct")
button_wrong = browser.find_element_by_id("button_wrong")
button_correct.click()

wanted_score = 42069
current_score = 0
while current_score < wanted_score:
    elem_x = browser.find_element_by_id("task_x")
    x = int(elem_x.text)
    elem_y = browser.find_element_by_id("task_y")
    y = int(elem_y.text)
    elem_expected_result = browser.find_element_by_id("task_res")
    expected_result = int(elem_expected_result.text)
    elem_op = browser.find_element_by_id("task_op")
    op = elem_op.text
    print("Score: " + str(current_score), end='\r')
    print("Progress: " + str(current_score/wanted_score), end='\r')
    if op == '+':
        if x + y == expected_result:
            button_correct.click()
        else:
            button_wrong.click()
    elif op == '–':
        if x - y == expected_result:
            button_correct.click()
        else:
            button_wrong.click()
    elif op == '×':
        if x * y == expected_result:
            button_correct.click()
        else:
            button_wrong.click()
    elif op == '/':
        if x / y == expected_result:
            button_correct.click()
        else:
            button_wrong.click()
    current_score = int(browser.find_element_by_id("score_value").text)
