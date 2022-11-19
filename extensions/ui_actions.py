import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from utilities.Base import Base


@allure.step("Update Text Element")
def update_text(element, text):
    Base.WAIT.until(EC.visibility_of(element))
    element.clear()
    element.send_keys(text)


@allure.step("Click On Element")
def click(element):
    Base.WAIT.until(EC.element_to_be_clickable(element))
    element.click()


@allure.step("Insert Key")
def insert_key(element, key):
    element.send_keys(key)


@allure.step("Get Text Of Element")
def get_element_text(element):
    return element.text


@allure.step("Select Option By Visible Text")
def select_element_by_text(element, text):
    Base.WAIT.until(EC.visibility_of(element))
    selector = Select(element)
    selector.select_by_visible_text(text)

