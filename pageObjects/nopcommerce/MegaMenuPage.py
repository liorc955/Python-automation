from seleniumpagefactory.Pagefactory import PageFactory


class MegaMenu(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        "btn_customers_prm": (
            "XPATH",
            "//ul[@class='nav nav-pills nav-sidebar flex-column nav-legacy']/*[4]",
        ),
        "btn_customers_sub": ("XPATH", "//li/a[@href='/Admin/Customer/List']"),
    }
