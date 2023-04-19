from selenium.webdriver.common.by import By

from page_objects.objects.ElementLocator import ElementLocator


class Login:

    def __init__(self, driver):
        self.driver = driver
        self.__text_user_email = ElementLocator(By.ID, "Email")
        self.__textbox_password = ElementLocator(By.ID, "Password")
        self.__button_login = ElementLocator(By.XPATH, "//button[@class='button-1 login-button']")

    @property
    def textbox_user_email(self):
        return self.driver.find_element(self.__text_user_email.by, self.__text_user_email.value)

    @property
    def textbox_password(self):
        return self.driver.find_element(self.__textbox_password.by, self.__textbox_password.value)

    @property
    def button_login(self):
        return self.driver.find_element(self.__button_login.by, self.__button_login.value)


"""    def login_action(self, email, password):
        self.textbox_user_email.clear_text()
        self.textbox_password.clear_text()
        self.textbox_user_email.send_keys(email)
        self.textbox_password.send_keys(password)
        self.button_login.click()"""
