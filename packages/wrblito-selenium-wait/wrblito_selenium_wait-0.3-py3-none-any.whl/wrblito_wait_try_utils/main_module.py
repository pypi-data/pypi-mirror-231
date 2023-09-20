from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def wait_and_click(self, by, value, condition=EC.presence_of_element_located, timeout=10):
    try:
        element = WebDriverWait(self, timeout).until(condition((by, value)))
        element.click()
    except Exception as e:
        print(f"An error occurred: {e}")

def wait_and_type(self, actions, by, value, text, condition=EC.presence_of_element_located, timeout=10):
    try:
        element = WebDriverWait(self, timeout).until(condition((by, value)))
        actions.move_to_element(element)
        actions.click()
        actions.send_keys(text)
        actions.perform()
    except Exception as e:
        print(f"An error occurred: {e}")