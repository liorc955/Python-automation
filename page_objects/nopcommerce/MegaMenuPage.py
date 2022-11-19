from selenium.webdriver.common.by import By

from page_objects.objects.ElementLocator import ElementLocator


class MegaMenu:
    BTN_CUSTOMERS_PRM = ElementLocator(By.XPATH, "//ul[@class='nav nav-pills nav-sidebar flex-column nav-legacy']/*[4]")
    BTN_CUSTOMERS_SUB = ElementLocator(By.XPATH, "//li/a[@href='/Admin/Customer/List']")

    def __init__(self, driver):
        self.driver = driver

    @property
    def btn_customers_prm(self):
        return self.driver.find_element(self.BTN_CUSTOMERS_PRM.by, self.BTN_CUSTOMERS_PRM.value)

    @property
    def btn_customers_sub(self):
        return self.driver.find_element(self.BTN_CUSTOMERS_SUB.by, self.BTN_CUSTOMERS_SUB.value)
