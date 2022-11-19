from selenium.webdriver.common.by import By

from page_objects.objects.ElementLocator import ElementLocator


class PushMenu:
    LINK_LOGOUT = ElementLocator(By.ID, "logout")

    def __init__(self, driver):
        self.driver = driver

    def link_logout(self):
        return self.driver.find_element(self.LINK_LOGOUT.by, self.LINK_LOGOUT.value)
