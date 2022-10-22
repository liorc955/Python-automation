from selenium.webdriver.common.by import By


class CreateCustomer:
    TEXTBOX_EMAIL = "Email"
    TEXTBOX_PASSWORD = "Password"
    TEXTBOX_FIRST_NAME = "FirstName"
    TEXTBOX_LAST_NAME = "LastName"
    TEXTBOX_GENDER_MALE = "Gender_Male"
    TEXTBOX_GENDER_FEMALE = "Gender_Female"
    TEXTBOX_DATEOFBIRTH = "DateOfBirth"
    TEXTBOX_COMPANY = "Company"
    CHECKBOX_TAXEXEMPT = "IsTaxExempt"
    DIV_NEWSLETTER = "(//div[@class='k-multiselect-wrap k-floatwrap'])[1]"
    LI_NEWSLETTER_TEST_STORE_2_OPT = "//*[@id='SelectedNewsletterSubscriptionStoreIds_listbox']/li[text()='Test store " \
                                     "2'] "
    DIV_CUSTOMER_ROLE = "(//div[@class='k-multiselect-wrap k-floatwrap'])[2]"
    LI_ADMINISTRATORS_ROLE_OPT = "//*[@id='SelectedCustomerRoleIds_listbox']/li[text()='Administrators']"
    SELECT_VENDOR_ID = "VendorId"
    CHECKBOX_ACTIVE = "Active"
    TEXTAREA_ADMIN_COMMENT = "AdminComment"
    BTN_SAVE = "save"
    BTN_SAVE_CONTINUE = "save-continue"

    def __init__(self, driver):
        self.driver = driver

    @property
    def textbox_email(self):
        return self.driver.find_element(By.ID, self.TEXTBOX_EMAIL)

    @property
    def textbox_password(self):
        return self.driver.find_element(By.ID, self.TEXTBOX_PASSWORD)

    @property
    def textbox_first_name(self):
        return self.driver.find_element(By.ID, self.TEXTBOX_FIRST_NAME)

    @property
    def textbox_last_name(self):
        return self.driver.find_element(By.ID, self.TEXTBOX_LAST_NAME)

    @property
    def textbox_gender_male(self):
        return self.driver.find_element(By.ID, self.TEXTBOX_GENDER_MALE)

    @property
    def textbox_gender_female(self):
        return self.driver.find_element(By.ID, self.TEXTBOX_GENDER_FEMALE)

    @property
    def textbox_dateOfBirth(self):
        return self.driver.find_element(By.ID, self.TEXTBOX_DATEOFBIRTH)

    @property
    def textbox_company(self):
        return self.driver.find_element(By.ID, self.TEXTBOX_COMPANY)

    @property
    def checkbox_taxExempt(self):
        return self.driver.find_element(By.ID, self.CHECKBOX_TAXEXEMPT)

    @property
    def div_newsletter(self):
        return self.driver.find_element(By.XPATH, self.DIV_NEWSLETTER)

    @property
    def li_newsletter_test_store_2_opt(self):
        return self.driver.find_element(By.XPATH, self.LI_NEWSLETTER_TEST_STORE_2_OPT)

    @property
    def div_customer_role(self):
        return self.driver.find_element(By.XPATH, self.DIV_CUSTOMER_ROLE)

    @property
    def li_Administrators_role_opt(self):
        return self.driver.find_element(By.XPATH, self.LI_ADMINISTRATORS_ROLE_OPT)

    @property
    def select_vendor_id(self):
        return self.driver.find_element(By.ID, self.SELECT_VENDOR_ID)

    @property
    def checkbox_active(self):
        return self.driver.find_element(By.ID, self.CHECKBOX_ACTIVE)

    @property
    def textarea_admin_comment(self):
        return self.driver.find_element(By.ID, self.TEXTAREA_ADMIN_COMMENT)

    @property
    def btn_save(self):
        return self.driver.find_element(By.NAME, self.BTN_SAVE)

    @property
    def btn_save_continue(self):
        return self.driver.find_element(By.NAME, self.BTN_SAVE_CONTINUE)


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
