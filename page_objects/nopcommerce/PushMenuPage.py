from selenium.webdriver.common.by import By

from page_objects.objects.ElementLocator import ElementLocator


class PushMenu:

    def __init__(self, driver):
        self.driver = driver
        self.__link_logout = ElementLocator(By.ID, "logout")

    def link_logout(self):
        return self.driver.find_element(self.__link_logout.by, self.__link_logout.value)
