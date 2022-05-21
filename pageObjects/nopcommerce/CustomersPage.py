from seleniumpagefactory.Pagefactory import PageFactory


class Customers(PageFactory):
    tblSearchResults_xpath = "//table[@role='grid']"
    table_xpath = "//table[@id='customers-grid']"
    tableRows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tableColumns_xpath = "//table[@id='customers-grid']//tbody/tr/td"
    table_xpath = "//table[@id='customers-grid']"

    def __init__(self, driver):
        self.driver = driver

    locators = {
        "btn_add_new": ("XPATH", "//div/*[@href='/Admin/Customer/Create']"),
        "div_customer_added_success": (
            "XPATH",
            "//*[@class='alert alert-success alert-dismissable']",
        ),
        "textbox_search_email": ("ID", "SearchEmail"),
        "textbox_search_firstName": ("ID", "SearchFirstName"),
        "textbox_search_lastName": ("ID", "SearchLastName"),
        "btn_search": ("ID", "search-customers"),
        "email_column_value": (
            "XPATH",
            "//table[@id='customers-grid']//tbody/tr/td[2]",
        ),
    }


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
