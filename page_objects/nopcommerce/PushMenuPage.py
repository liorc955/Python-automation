from seleniumpagefactory.Pagefactory import PageFactory


class PushMenu(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {"link_logout": ("ID", "logout")}
