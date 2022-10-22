import json

import allure
import random
import string
import time
import pytest
from extensions import ui_actions
from utilities.Base import Base
from utilities.cv_util import read_data
from workflows import web_flows

path = "./TestData/credentials.csv"


def random_generator(size=8, char=string.ascii_lowercase + string.digits):
    return "".join(random.choice(char) for x in range(size))


@allure.description("This test verifies the home title page")
def test01_homePageTitle():
    assert Base.DRIVER.title == "Your store. Login", "There is a problem on the attempt to enter the site"


@allure.description("This test verifies login by DDT parameters")
@pytest.mark.parametrize("email_data,password_data,expected_result", read_data(path))
def test02_login_ddt(email_data, password_data, expected_result):
    web_flows.login(email_data, password_data)
    if expected_result == "pass":
        assert Base.DRIVER.title == "Dashboard / nopCommerce administration", "Incorrect title for this username and " \
                                                                              "password "
    elif expected_result == "failed":
        assert Base.DRIVER.title == "Your store. Login", "Incorrect title for this username and password"


@allure.description("This test verifies the search of customer by email flow")
def test03_search_customer_by_email(login_before):
    web_flows.goto_customer_table()
    email = "steve_gates@nopCommerce.com"
    web_flows.search_for_email(email)
    time.sleep(2)
    assert web_flows.get_column_number() > 1
    assert email == ui_actions.get_element_text(Base.CUSTOMER.email_column_value), "Incorrect email for this customer"


@allure.description("This test verifies the search of customer by name flow")
def test04_search_customer_by_name(login_before):
    web_flows.goto_customer_table()
    firstname = "Steve"
    lastname = "Gates"
    web_flows.search_for_name(firstname, lastname)
    time.sleep(2)
    assert web_flows.get_column_number() > 1, "Can't find any customer with this name"
    assert web_flows.search_name_on_table(firstname + " " + lastname), "The first and last name of this customer is " \
                                                                       "incorrect "


@allure.description("This test verifies the add of a new customer flow")
def test05_add_new_customer(login_before):
    web_flows.goto_customer_table()
    ui_actions.click(Base.CUSTOMER.btn_add_new)
    customer = json.loads(open('./TestData/customer.json', "r").read())
    customer['email'] = customer['email'].format(random=random_generator())
    customer['tax_exempt'] = customer['tax_exempt'] in ('True', 'true')
    customer['active'] = customer['active'] in ('True', 'true')
    web_flows.fill_customer_form(customer)
    ui_actions.click(Base.CREATE_CUSTOMER.btn_save)
    assert (
            Base.DRIVER.title == "Customers / nopCommerce administration"
            and "The new customer has been added successfully."
            in ui_actions.get_element_text(Base.CUSTOMER.div_customer_added_success), "There is a problem while "
                                                                                      "trying to submit the form "
    )
