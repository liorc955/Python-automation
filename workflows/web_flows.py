import allure
from selenium.webdriver.common.by import By

from extensions import ui_actions


@allure.step("Business Flow: Login")
def login(pages, wait, email, password):
    login_page = pages["login"]
    ui_actions.update_text(wait, login_page.textbox_user_email, email)
    ui_actions.update_text(wait, login_page.textbox_password, password)
    ui_actions.click(wait, login_page.button_login)


@allure.step("Business Flow: Search By Email")
def search_for_email(pages, wait, email):
    customer = pages["customer"]
    ui_actions.update_text(wait, customer.textbox_search_email, email)
    ui_actions.click(wait, customer.btn_search)


@allure.step("Business Flow: Search By Name")
def search_for_name(pages, wait, first_name, last_name):
    customer = pages["customer"]
    ui_actions.update_text(wait, customer.textbox_search_firstName, first_name)
    ui_actions.update_text(wait, customer.textbox_search_lastName, last_name)
    ui_actions.click(wait, customer.btn_search)


@allure.step("Business Flow: Get Row Number")
def get_row_number(pages, driver):
    return len(driver.find_elements(By.XPATH, pages["customer"].tableRows_xpath))


@allure.step("Business Flow: Get Column Number")
def get_column_number(pages, driver):
    return len(driver.find_elements(By.XPATH, pages["customer"].tableColumns_xpath))


@allure.step("Business Flow: Search For Name")
def search_name_on_table(pages, driver, full_name):
    customer = pages["customer"]
    flag = False
    for r in range(1, get_row_number(pages, driver) + 1):
        table = driver.find_element(By.XPATH, customer.table_xpath)
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
def goto_customer_table(pages, wait):
    mega_menu = pages["mega_menu"]
    ui_actions.click(wait, mega_menu.btn_customers_prm)
    ui_actions.click(wait, mega_menu.btn_customers_sub)


@allure.step("Business Flow: Fill In Customer Form")
def fill_customer_form(
        pages,
        wait,
        email,
        password,
        firstname,
        lastname,
        gender,
        date_birth,
        company,
        tax_exempt,
        newsletter,
        role,
        vendor_id,
        active,
        comment,
):
    create_customer = pages["create_customer"]
    ui_actions.update_text(wait, create_customer.textbox_email, email)
    ui_actions.update_text(wait, create_customer.textbox_password, password)
    ui_actions.update_text(wait, create_customer.textbox_first_name, firstname)
    ui_actions.update_text(wait, create_customer.textbox_last_name, lastname)
    if gender == "male":
        ui_actions.click(wait, create_customer.textbox_gender_male)
    elif gender == "female":
        ui_actions.click(wait, create_customer.textbox_gender_female)
    ui_actions.update_text(wait, create_customer.textbox_dateOfBirth, date_birth)
    ui_actions.update_text(wait, create_customer.textbox_company, company)
    if tax_exempt:
        ui_actions.click(wait, create_customer.checkbox_taxExempt)
    ui_actions.click(wait, create_customer.div_newsletter)
    if newsletter == "Test store 2":
        ui_actions.click(wait, create_customer.li_newsletter_test_store_2_opt)
    ui_actions.click(wait, create_customer.div_customer_role)
    if role == "Administrators":
        ui_actions.click(wait, create_customer.li_Administrators_role_opt)
    create_customer.select_vendor_id.select_element_by_text(vendor_id)
    if not active:
        ui_actions.click(wait, create_customer.checkbox_active)
    ui_actions.update_text(wait, create_customer.textarea_admin_comment, comment)
