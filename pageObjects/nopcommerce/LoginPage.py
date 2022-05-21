from seleniumpagefactory.Pagefactory import PageFactory


class Login(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        "textbox_user_email": ("ID", "Email"),
        "textbox_password": ("ID", "Password"),
        "button_login": ("XPATH", "//button[@class='button-1 login-button']"),
    }


"""    def login_action(self, email, password):
        self.textbox_user_email.clear_text()
        self.textbox_password.clear_text()
        self.textbox_user_email.send_keys(email)
        self.textbox_password.send_keys(password)
        self.button_login.click()"""
