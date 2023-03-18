from selenium.webdriver.common.by import By

from page_objects.objects.ElementLocator import ElementLocator


class Customers:

    def __init__(self, driver):
        self.driver = driver
        self._table_search_result = ElementLocator(By.XPATH, "//table[@role='grid']")
        self._table_rows = ElementLocator(By.XPATH, "//table[@id='customers-grid']//tbody/tr")
        self._table_columns = ElementLocator(By.XPATH, "//table[@id='customers-grid']//tbody/tr/td")
        self._table = ElementLocator(By.XPATH, "//table[@id='customers-grid']")
        self._btn_add_new = ElementLocator(By.XPATH, "//div/*[@href='/Admin/Customer/Create']")
        self._div_customer_added_success = ElementLocator(By.XPATH, "//*[@class='alert alert-success alert-dismissable']")
        self._textbox_search_email = ElementLocator(By.ID, "SearchEmail")
        self._textbox_search_firstname = ElementLocator(By.ID, "SearchFirstName")
        self._textbox_search_lastname = ElementLocator(By.ID, "SearchLastName")
        self._btn_search = ElementLocator(By.ID, "search-customers")
        self._email_column_value = ElementLocator(By.XPATH, "//table[@id='customers-grid']//tbody/tr/td[2]")

    @property
    def btn_add_new(self):
        return self.driver.find_element(self._btn_add_new.by, self._btn_add_new.value)

    @property
    def div_customer_added_success(self):
        return self.driver.find_element(self._div_customer_added_success.by, self._div_customer_added_success.value)

    @property
    def textbox_search_email(self):
        return self.driver.find_element(self._textbox_search_email.by, self._textbox_search_email.value)

    @property
    def textbox_search_firstName(self):
        return self.driver.find_element(self._textbox_search_firstname.by, self._textbox_search_firstname.value)

    @property
    def textbox_search_lastName(self):
        return self.driver.find_element(self._textbox_search_lastname.by, self._textbox_search_lastname.value)

    @property
    def btn_search(self):
        return self.driver.find_element(self._btn_search.by, self._btn_search.value)

    @property
    def email_column_value(self):
        return self.driver.find_element(self._email_column_value.by,  self._email_column_value.value)

    @property
    def table(self):
        return self.driver.find_element(self._table.by, self._table.value)

    @property
    def get_row_number(self):
        return len(self.driver.find_elements(self._table_rows.by, self._table_rows.value))

    @property
    def get_column_number(self):
        return len(self.driver.find_elements(self._table_columns.by, self._table_columns.value))


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
