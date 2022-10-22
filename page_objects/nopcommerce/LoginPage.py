from selenium.webdriver.common.by import By


class Login:
    TEXT_USER_EMAIL = "Email"
    TEXTBOX_PASSWORD = "Password"
    BUTTON_LOGIN = "//button[@class='button-1 login-button']"

    def __init__(self, driver):
        self.driver = driver

    @property
    def textbox_user_email(self):
        return self.driver.find_element(By.ID, self.TEXT_USER_EMAIL)

    @property
    def textbox_password(self):
        return self.driver.find_element(By.ID, self.TEXTBOX_PASSWORD)

    @property
    def button_login(self):
        return self.driver.find_element(By.XPATH, self.BUTTON_LOGIN)


"""    def login_action(self, email, password):
        self.textbox_user_email.clear_text()
        self.textbox_password.clear_text()
        self.textbox_user_email.send_keys(email)
        self.textbox_password.send_keys(password)
        self.button_login.click()"""
