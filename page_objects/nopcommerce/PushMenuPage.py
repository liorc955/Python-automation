from selenium.webdriver.common.by import By


class PushMenu:
    LINK_LOGOUT = 'logout'

    def __init__(self, driver):
        self.driver = driver

    def link_logout(self):
        return self.driver.find_element(By.ID, self.LINK_LOGOUT)
