from selenium.webdriver.common.by import By

from page_objects.objects.ElementLocator import ElementLocator


class Login:
    TEXT_USER_EMAIL = ElementLocator(By.ID, "Email")
    TEXTBOX_PASSWORD = ElementLocator(By.ID, "Password")
    BUTTON_LOGIN = ElementLocator(By.XPATH, "//button[@class='button-1 login-button']")

    def __init__(self, driver):
        self.driver = driver

    @property
    def textbox_user_email(self):
        return self.driver.find_element(self.TEXT_USER_EMAIL.by, self.TEXT_USER_EMAIL.value)

    @property
    def textbox_password(self):
        return self.driver.find_element(self.TEXTBOX_PASSWORD.by, self.TEXTBOX_PASSWORD.value)

    @property
    def button_login(self):
        return self.driver.find_element(self.BUTTON_LOGIN.by, self.BUTTON_LOGIN.value)


"""    def login_action(self, email, password):
        self.textbox_user_email.clear_text()
        self.textbox_password.clear_text()
        self.textbox_user_email.send_keys(email)
        self.textbox_password.send_keys(password)
        self.button_login.click()"""
