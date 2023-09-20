from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def element_click(driver, type, element):
    while True:
        if driver.find_elements(type, element):
            driver.find_element(type, element).click()
            break

def element_type(driver, actions, type, element, text):
    while True:
        if driver.find_elements(type, element):
            element = driver.find_element(type, element)
            actions.move_to_element(element)
            actions.click()
            actions.send_keys(text)
            actions.perform()
            break