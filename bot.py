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

wanted_score = 20
current_score = 0
while current_score < wanted_score:
    x = int(browser.find_element_by_id("task_x").text)
    y = int(browser.find_element_by_id("task_y").text)
    expected_result = int(browser.find_element_by_id("task_res").text)
    op = browser.find_element_by_id("task_op").text
    print("Progress: " + str(current_score/wanted_score), end='\r')
    correct = False
    if op == '+': correct = x + y == expected_result
    elif op == '–': correct = x - y == expected_result
    elif op == '×': correct =  x * y == expected_result
    elif op == '/': correct = x / y == expected_result
    
    if correct: button_correct.click()
    else: button_wrong.click()
    current_score = int(browser.find_element_by_id("score_value").text)
