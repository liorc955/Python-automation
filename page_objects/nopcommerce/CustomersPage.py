from selenium.webdriver.common.by import By

from page_objects.objects.ElementLocator import ElementLocator


class Customers:

    def __init__(self, driver):
        self.driver = driver
        self.__table_search_result = ElementLocator(By.XPATH, "//table[@role='grid']")
        self.__table_rows = ElementLocator(By.XPATH, "//table[@id='customers-grid']//tbody/tr")
        self.__table_columns = ElementLocator(By.XPATH, "//table[@id='customers-grid']//tbody/tr/td")
        self.__table = ElementLocator(By.XPATH, "//table[@id='customers-grid']")
        self.__btn_add_new = ElementLocator(By.XPATH, "//div/*[@href='/Admin/Customer/Create']")
        self.__div_customer_added_success = ElementLocator(By.XPATH, "//*[@class='alert alert-success alert-dismissable']")
        self.__textbox_search_email = ElementLocator(By.ID, "SearchEmail")
        self.__textbox_search_firstname = ElementLocator(By.ID, "SearchFirstName")
        self.__textbox_search_lastname = ElementLocator(By.ID, "SearchLastName")
        self.__btn_search = ElementLocator(By.ID, "search-customers")
        self.__email_column_value = ElementLocator(By.XPATH, "//table[@id='customers-grid']//tbody/tr/td[2]")

    @property
    def btn_add_new(self):
        return self.driver.find_element(self.__btn_add_new.by, self.__btn_add_new.value)

    @property
    def div_customer_added_success(self):
        return self.driver.find_element(self.__div_customer_added_success.by, self.__div_customer_added_success.value)

    @property
    def textbox_search_email(self):
        return self.driver.find_element(self.__textbox_search_email.by, self.__textbox_search_email.value)

    @property
    def textbox_search_firstName(self):
        return self.driver.find_element(self.__textbox_search_firstname.by, self.__textbox_search_firstname.value)

    @property
    def textbox_search_lastName(self):
        return self.driver.find_element(self.__textbox_search_lastname.by, self.__textbox_search_lastname.value)

    @property
    def btn_search(self):
        return self.driver.find_element(self.__btn_search.by, self.__btn_search.value)

    @property
    def email_column_value(self):
        return self.driver.find_element(self.__email_column_value.by,  self.__email_column_value.value)

    @property
    def table(self):
        return self.driver.find_element(self.__table.by, self.__table.value)

    @property
    def get_row_number(self):
        return len(self.driver.find_elements(self.__table_rows.by, self.__table_rows.value))

    @property
    def get_column_number(self):
        return len(self.driver.find_elements(self.__table_columns.by, self.__table_columns.value))


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
