from selenium.webdriver.common.by import By

from page_objects.objects.ElementLocator import ElementLocator


class MegaMenu:

    def __init__(self, driver):
        self.driver = driver
        self._btn_customers_prm  = ElementLocator(By.XPATH, "//ul[@class='nav nav-pills nav-sidebar flex-column nav-legacy']/*[4]")
        self._btn_customers_sub = ElementLocator(By.XPATH, "//li/a[@href='/Admin/Customer/List']")

    @property
    def btn_customers_prm(self):
        return self.driver.find_element(self._btn_customers_prm.by, self._btn_customers_prm.value)

    @property
    def btn_customers_sub(self):
        return self.driver.find_element(self._btn_customers_sub.by, self._btn_customers_sub.value)
