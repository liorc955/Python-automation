from selenium.webdriver.common.by import By


class Customers:
    tblSearchResults_xpath = "//table[@role='grid']"
    table_xpath = "//table[@id='customers-grid']"
    tableRows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tableColumns_xpath = "//table[@id='customers-grid']//tbody/tr/td"
    table_xpath = "//table[@id='customers-grid']"
    BTN_ADD_NEW = "//div/*[@href='/Admin/Customer/Create']"
    DIV_CUSTOMER_ADDED_SUCCESS = "//*[@class='alert alert-success alert-dismissable']"
    TEXTBOX_SEARCH_EMAIL = "SearchEmail"
    TEXTBOX_SEARCH_FIRSTNAME = "SearchFirstName"
    TEXTBOX_SEARCH_LASTNAME = "SearchLastName"
    BTN_SEARCH = "search-customers"
    EMAIL_COLUMN_VALUE = "//table[@id='customers-grid']//tbody/tr/td[2]"

    def __init__(self, driver):
        self.driver = driver

    @property
    def btn_add_new(self):
        return self.driver.find_element(By.XPATH, self.BTN_ADD_NEW)

    @property
    def div_customer_added_success(self):
        return self.driver.find_element(By.XPATH, self.DIV_CUSTOMER_ADDED_SUCCESS)

    @property
    def textbox_search_email(self):
        return self.driver.find_element(By.ID, self.TEXTBOX_SEARCH_EMAIL)

    @property
    def textbox_search_firstName(self):
        return self.driver.find_element(By.ID, self.TEXTBOX_SEARCH_FIRSTNAME)

    @property
    def textbox_search_lastName(self):
        return self.driver.find_element(By.ID, self.TEXTBOX_SEARCH_LASTNAME)

    @property
    def btn_search(self):
        return self.driver.find_element(By.ID, self.BTN_SEARCH)

    @property
    def email_column_value(self):
        return self.driver.find_element(By.XPATH, self.EMAIL_COLUMN_VALUE)


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
