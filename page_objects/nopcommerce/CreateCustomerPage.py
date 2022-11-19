from selenium.webdriver.common.by import By

from page_objects.objects.ElementLocator import ElementLocator


class CreateCustomer:
    TEXTBOX_EMAIL = ElementLocator(By.ID, "Email")
    TEXTBOX_PASSWORD = ElementLocator(By.ID, "Password")
    TEXTBOX_FIRST_NAME = ElementLocator(By.ID, "FirstName")
    TEXTBOX_LAST_NAME = ElementLocator(By.ID, "LastName")
    TEXTBOX_GENDER_MALE = ElementLocator(By.ID, "Gender_Male")
    TEXTBOX_GENDER_FEMALE = ElementLocator(By.ID, "Gender_Female")
    TEXTBOX_DATEOFBIRTH = ElementLocator(By.ID, "DateOfBirth")
    TEXTBOX_COMPANY = ElementLocator(By.ID, "Company")
    CHECKBOX_TAXEXEMPT = ElementLocator(By.ID, "IsTaxExempt")
    DIV_NEWSLETTER = ElementLocator(By.XPATH, "(//div[@class='k-multiselect-wrap k-floatwrap'])[1]")
    LI_NEWSLETTER_TEST_STORE_2_OPT = ElementLocator(By.XPATH, "//*["
                                                              "@id='SelectedNewsletterSubscriptionStoreIds_listbox"
                                                              "']/li[text()='Test store "
                                                              "2'] ")
    DIV_CUSTOMER_ROLE = ElementLocator(By.XPATH, "(//div[@class='k-multiselect-wrap k-floatwrap'])[2]")
    LI_ADMINISTRATORS_ROLE_OPT = ElementLocator(By.XPATH, "//*[@id='SelectedCustomerRoleIds_listbox']/li[text("
                                                          ")='Administrators']")
    SELECT_VENDOR_ID = ElementLocator(By.ID, "VendorId")
    CHECKBOX_ACTIVE = ElementLocator(By.ID, "Active")
    TEXTAREA_ADMIN_COMMENT = ElementLocator(By.ID, "AdminComment")
    BTN_SAVE = ElementLocator(By.NAME, "save")
    BTN_SAVE_CONTINUE = ElementLocator(By.NAME, "save-continue")

    def __init__(self, driver):
        self.driver = driver

    @property
    def textbox_email(self):
        return self.driver.find_element(self.TEXTBOX_EMAIL.by, self.TEXTBOX_EMAIL.value)

    @property
    def textbox_password(self):
        return self.driver.find_element(self.TEXTBOX_PASSWORD.by, self.TEXTBOX_PASSWORD.value)

    @property
    def textbox_first_name(self):
        return self.driver.find_element(self.TEXTBOX_FIRST_NAME.by, self.TEXTBOX_FIRST_NAME.value)

    @property
    def textbox_last_name(self):
        return self.driver.find_element(self.TEXTBOX_LAST_NAME.by, self.TEXTBOX_LAST_NAME.value)

    @property
    def textbox_gender_male(self):
        return self.driver.find_element(self.TEXTBOX_GENDER_MALE.by, self.TEXTBOX_GENDER_MALE.value)

    @property
    def textbox_gender_female(self):
        return self.driver.find_element(self.TEXTBOX_GENDER_FEMALE.by, self.TEXTBOX_GENDER_FEMALE.value)

    @property
    def textbox_dateOfBirth(self):
        return self.driver.find_element(self.TEXTBOX_DATEOFBIRTH.by, self.TEXTBOX_DATEOFBIRTH.value)

    @property
    def textbox_company(self):
        return self.driver.find_element(self.TEXTBOX_COMPANY.by, self.TEXTBOX_COMPANY.value)

    @property
    def checkbox_taxExempt(self):
        return self.driver.find_element(self.CHECKBOX_TAXEXEMPT.by, self.CHECKBOX_TAXEXEMPT.value)

    @property
    def div_newsletter(self):
        return self.driver.find_element(self.DIV_NEWSLETTER.by, self.DIV_NEWSLETTER.value)

    @property
    def li_newsletter_test_store_2_opt(self):
        return self.driver.find_element(
            self.LI_NEWSLETTER_TEST_STORE_2_OPT.by, self.LI_NEWSLETTER_TEST_STORE_2_OPT.value)

    @property
    def div_customer_role(self):
        return self.driver.find_element(self.DIV_CUSTOMER_ROLE.by, self.DIV_CUSTOMER_ROLE.value)

    @property
    def li_Administrators_role_opt(self):
        return self.driver.find_element(self.LI_ADMINISTRATORS_ROLE_OPT.by, self.LI_ADMINISTRATORS_ROLE_OPT.value)

    @property
    def select_vendor_id(self):
        return self.driver.find_element(self.SELECT_VENDOR_ID.by, self.SELECT_VENDOR_ID.value)

    @property
    def checkbox_active(self):
        return self.driver.find_element(self.CHECKBOX_ACTIVE.by, self.CHECKBOX_ACTIVE.value)

    @property
    def textarea_admin_comment(self):
        return self.driver.find_element(self.TEXTAREA_ADMIN_COMMENT.by, self.TEXTAREA_ADMIN_COMMENT.value)

    @property
    def btn_save(self):
        return self.driver.find_element(self.BTN_SAVE.by, self.BTN_SAVE.value)

    @property
    def btn_save_continue(self):
        return self.driver.find_element(self.BTN_SAVE_CONTINUE.by, self.BTN_SAVE_CONTINUE.value)


"""    def fill_customer_form_action(
        self,
        email,
        password,
        firstname,
        lastname,
        gender,
        date_birth,
        company,
        tax_exempt,
        newsletter,
        role,
        vendor_id,
        active,
        comment,
    ):
        self.textbox_email.send_keys(email)
        self.textbox_password.send_keys(password)
        self.textbox_first_name.send_keys(firstname)
        self.textbox_last_name.send_keys(lastname)
        if gender == "male":
            self.textbox_gender_male.click()
        elif gender == "female":
            self.textbox_gender_female.click()
        self.textbox_dateOfBirth.send_keys(date_birth)
        self.textbox_company.send_keys(company)
        if tax_exempt:
            self.checkbox_taxExempt.click()
        self.div_newsletter.click()
        if newsletter == "Test store 2":
            self.li_newsletter_test_store_2_opt.click()
        self.div_customer_role.click()
        if role == "Administrators":
            self.li_Administrators_role_opt.click()
        self.select_vendor_id.select_element_by_text(vendor_id)
        if not active:
            self.checkbox_active.click()
        self.textarea_admin_comment.send_keys(comment)"""
