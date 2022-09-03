import allure
from selenium.webdriver.support import expected_conditions as EC


@allure.step("Update Text Element")
def update_text(wait, element, text):
    wait.until(EC.visibility_of(element))
    element.clear()
    element.send_keys(text)


@allure.step("Click On Element")
def click(wait, element):
    wait.until(EC.element_to_be_clickable(element))
    element.click()


@allure.step("Insert Key")
def insert_key(element, key):
    element.send_keys(key)


@allure.step("Get Text Of Element")
def get_element_text(element):
    return element.text
