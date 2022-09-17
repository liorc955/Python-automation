import allure
import random
import string
import time
import pytest
from extensions import uiActions
from utilities.cvUtil import readData
from workflows import webFlows

path = "./TestData/credentials.csv"


def random_generator(size=8, char=string.ascii_lowercase + string.digits):
    return "".join(random.choice(char) for x in range(size))


@allure.description("This test verifies the home title page")
def test01_homePageTitle(setup):
    driver = setup
    assert driver.title == "Your store. Login"


@allure.description("This test verifies login by DDT parameters")
@pytest.mark.parametrize("email_data,password_data,expected_result", readData(path))
def test02_login_ddt(wait, pages, setup, email_data, password_data, expected_result):
    driver = setup
    webFlows.login(pages, wait, email_data, password_data)
    if expected_result == "pass":
        assert driver.title == "Dashboard / nopCommerce administration"
    elif expected_result == "failed":
        assert driver.title == "Your store. Login"


@allure.description("This test verifies the search of customer by email flow")
def test03_search_customer_by_email(login_before, pages, wait, setup):
    driver = setup
    customer = pages["customer"]
    webFlows.goto_customer_table(pages, wait)
    email = "steve_gates@nopCommerce.com"
    webFlows.search_for_email(pages, wait, email)
    time.sleep(2)
    assert webFlows.get_column_number(pages, driver) > 1
    assert email == uiActions.get_element_text(customer.email_column_value)


@allure.description("This test verifies the search of customer by name flow")
def test04_search_customer_by_name(login_before, pages, wait, setup):
    driver = setup
    webFlows.goto_customer_table(pages, wait)
    firstname = "Steve"
    lastname = "Gates"
    webFlows.search_for_name(pages, wait, firstname, lastname)
    time.sleep(2)
    assert webFlows.get_column_number(pages, driver) > 1
    assert webFlows.search_name_on_table(pages, driver, firstname + " " + lastname)


@allure.description("This test verifies the add of a new customer flow")
def test05_add_new_customer(login_before, pages, wait, setup):
    driver = setup
    customer = pages["customer"]
    create_customer = pages["create_customer"]
    webFlows.goto_customer_table(pages, wait)
    uiActions.click(wait, customer.btn_add_new)
    webFlows.fill_customer_form(
        pages,
        wait,
        random_generator() + "@gmail.com",
        "Aa123456",
        "tt",
        "fdsf",
        "female",
        "4/1/2022",
        "tret",
        True,
        "Test store 2",
        "Administrators",
        "Vendor 1",
        True,
        "ddsfg",
    )
    uiActions.click(wait, create_customer.btn_save)
    assert (
        driver.title == "Customers / nopCommerce administration"
        and "The new customer has been added successfully."
        in uiActions.get_element_text(customer.div_customer_added_success)
    )
