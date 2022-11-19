import allure
from selenium.webdriver.common.by import By

from extensions import ui_actions
from utilities.Base import Base


@allure.step("Business Flow: Login")
def login(email, password):
    ui_actions.update_text(Base.LOGIN_PAGE.textbox_user_email, email)
    ui_actions.update_text(Base.LOGIN_PAGE.textbox_password, password)
    ui_actions.click(Base.LOGIN_PAGE.button_login)


@allure.step("Business Flow: Search By Email")
def search_for_email(email):
    ui_actions.update_text(Base.CUSTOMER.textbox_search_email, email)
    ui_actions.click(Base.CUSTOMER.btn_search)


@allure.step("Business Flow: Search By Name")
def search_for_name(first_name, last_name):
    ui_actions.update_text(Base.CUSTOMER.textbox_search_firstName, first_name)
    ui_actions.update_text(Base.CUSTOMER.textbox_search_lastName, last_name)
    ui_actions.click(Base.CUSTOMER.btn_search)


@allure.step("Business Flow: Search For Name")
def search_name_on_table(full_name):
    flag = False
    for r in range(1, Base.CUSTOMER.get_row_number + 1):
        table = Base.CUSTOMER.table
        name = ui_actions.get_element_text(
            table.find_element(
                By.XPATH,
                "//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[3]",
            )
        )
        if name == full_name:
            flag = True
            break
    return flag


@allure.step("Business Flow: Navigate To The Customer Table Page")
def goto_customer_table():
    ui_actions.click(Base.MEGA_MENU.btn_customers_prm)
    ui_actions.click(Base.MEGA_MENU.btn_customers_sub)


@allure.step("Business Flow: Fill In Customer Form")
def fill_customer_form(customer):
    ui_actions.update_text(Base.CREATE_CUSTOMER.textbox_email, customer['email'])
    ui_actions.update_text(Base.CREATE_CUSTOMER.textbox_password, customer['password'])
    ui_actions.update_text(Base.CREATE_CUSTOMER.textbox_first_name, customer['first_name'])
    ui_actions.update_text(Base.CREATE_CUSTOMER.textbox_last_name, customer['last_name'])
    if customer['gender'] == "male":
        ui_actions.click(Base.CREATE_CUSTOMER.textbox_gender_male)
    elif customer['gender'] == "female":
        ui_actions.click(Base.CREATE_CUSTOMER.textbox_gender_female)
    ui_actions.update_text(Base.CREATE_CUSTOMER.textbox_dateOfBirth, customer['date_birth'])
    ui_actions.update_text(Base.CREATE_CUSTOMER.textbox_company, customer['company'])
    if customer['tax_exempt']:
        ui_actions.click(Base.CREATE_CUSTOMER.checkbox_taxExempt)
    ui_actions.click(Base.CREATE_CUSTOMER.div_newsletter)
    if customer['newsletter'] == "Test store 2":
        ui_actions.click(Base.CREATE_CUSTOMER.li_newsletter_test_store_2_opt)
    ui_actions.click(Base.CREATE_CUSTOMER.div_customer_role)
    if customer['role'] == "Administrators":
        ui_actions.click(Base.CREATE_CUSTOMER.li_Administrators_role_opt)
    ui_actions.select_element_by_text(Base.CREATE_CUSTOMER.select_vendor_id, customer['vendor_id'])
    if not customer['active']:
        ui_actions.click(Base.CREATE_CUSTOMER.checkbox_active)
    ui_actions.update_text(Base.CREATE_CUSTOMER.textarea_admin_comment, customer['comment'])
