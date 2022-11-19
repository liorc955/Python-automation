from selenium.webdriver.common.by import By

from page_objects.objects.ElementLocator import ElementLocator


class Customers:
    TABLE_SEARCH_RESULT = ElementLocator(By.XPATH, "//table[@role='grid']")
    TABLE_ROWS = ElementLocator(By.XPATH, "//table[@id='customers-grid']//tbody/tr")
    TABLE_COLUMNS = ElementLocator(By.XPATH, "//table[@id='customers-grid']//tbody/tr/td")
    TABLE = ElementLocator(By.XPATH, "//table[@id='customers-grid']")
    BTN_ADD_NEW = ElementLocator(By.XPATH, "//div/*[@href='/Admin/Customer/Create']")
    DIV_CUSTOMER_ADDED_SUCCESS = ElementLocator(By.XPATH, "//*[@class='alert alert-success alert-dismissable']")
    TEXTBOX_SEARCH_EMAIL = ElementLocator(By.ID, "SearchEmail")
    TEXTBOX_SEARCH_FIRSTNAME = ElementLocator(By.ID, "SearchFirstName")
    TEXTBOX_SEARCH_LASTNAME = ElementLocator(By.ID, "SearchLastName")
    BTN_SEARCH = ElementLocator(By.ID, "search-customers")
    EMAIL_COLUMN_VALUE = ElementLocator(By.XPATH, "//table[@id='customers-grid']//tbody/tr/td[2]")

    def __init__(self, driver):
        self.driver = driver

    @property
    def btn_add_new(self):
        return self.driver.find_element(self.BTN_ADD_NEW.by, self.BTN_ADD_NEW.value)

    @property
    def div_customer_added_success(self):
        return self.driver.find_element(self.DIV_CUSTOMER_ADDED_SUCCESS.by, self.DIV_CUSTOMER_ADDED_SUCCESS.value)

    @property
    def textbox_search_email(self):
        return self.driver.find_element(self.TEXTBOX_SEARCH_EMAIL.by, self.TEXTBOX_SEARCH_EMAIL.value)

    @property
    def textbox_search_firstName(self):
        return self.driver.find_element(self.TEXTBOX_SEARCH_FIRSTNAME.by, self.TEXTBOX_SEARCH_FIRSTNAME.value)

    @property
    def textbox_search_lastName(self):
        return self.driver.find_element(self.TEXTBOX_SEARCH_LASTNAME.by, self.TEXTBOX_SEARCH_LASTNAME.value)

    @property
    def btn_search(self):
        return self.driver.find_element(self.BTN_SEARCH.by, self.BTN_SEARCH.value)

    @property
    def email_column_value(self):
        return self.driver.find_element(self.EMAIL_COLUMN_VALUE.by,  self.EMAIL_COLUMN_VALUE.value)

    @property
    def table(self):
        return self.driver.find_element(self.TABLE.by, self.TABLE.value)

    @property
    def get_row_number(self):
        return len(self.driver.find_elements(self.TABLE_ROWS.by, self.TABLE_ROWS.value))

    @property
    def get_column_number(self):
        return len(self.driver.find_elements(self.TABLE_COLUMNS.by, self.TABLE_COLUMNS.value))


"""    def searchForName_action(self, first_name, last_name):
        self.textbox_search_firstName.send_keys(first_name)
        self.textbox_search_lastName.send_keys(last_name)
        self.btn_search.click()

    def searchForEmail_action(self, email):
        self.textbox_search_email.send_keys(email)
        self.btn_search.click()

    def searchEmailOnTable_action(self, email):
        flag = False
        for r in range(1, self.getRowNumber() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            email_id = table.find_element(
                By.XPATH, "//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[2]"
            ).text
            if email_id == email:
                flag = True
                break
        return flag

    def searchNameOnTable_action(self, full_name):
        flag = False
        for r in range(1, self.getRowNumber() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            name = table.find_element(
                By.XPATH, "//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[3]"
            ).text
            if name == full_name:
                flag = True
                break
        return flag

    def getRowNumber(self):
        return len(self.driver.find_elements(By.XPATH, self.tableRows_xpath))

    def getColumnNumber(self):
        return len(self.driver.find_elements(By.XPATH, self.tableColumns_xpath))"""
