from selenium.webdriver.common.by import By


class MegaMenu:
    BTN_CUSTOMERS_PRM = "//ul[@class='nav nav-pills nav-sidebar flex-column nav-legacy']/*[4]"
    BTN_CUSTOMERS_SUB = "//li/a[@href='/Admin/Customer/List']"

    def __init__(self, driver):
        self.driver = driver

    @property
    def btn_customers_prm(self):
        return self.driver.find_element(By.XPATH, self.BTN_CUSTOMERS_PRM)

    @property
    def btn_customers_sub(self):
        return self.driver.find_element(By.XPATH, self.BTN_CUSTOMERS_SUB)
