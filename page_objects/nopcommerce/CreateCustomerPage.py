from selenium.webdriver.common.by import By

from page_objects.objects.ElementLocator import ElementLocator


class CreateCustomer:

    def __init__(self, driver):
        self.driver = driver
        self.__textbox_email = ElementLocator(By.ID, "Email")
        self.__textbox_password = ElementLocator(By.ID, "Password")
        self.__textbox_first_name = ElementLocator(By.ID, "FirstName")
        self.__textbox_last_name = ElementLocator(By.ID, "LastName")
        self.__textbox_gender_male = ElementLocator(By.ID, "Gender_Male")
        self.__textbox_gender_female = ElementLocator(By.ID, "Gender_Female")
        self.__textbox_dateofbirth = ElementLocator(By.ID, "DateOfBirth")
        self.__textbox_company = ElementLocator(By.ID, "Company")
        self.__checkbox_taxexempt = ElementLocator(By.ID, "IsTaxExempt")
        self.__div_newsletter = ElementLocator(By.XPATH, "(//div[@class='k-multiselect-wrap k-floatwrap'])[1]")
        self.__li_newsletter_test_store_2_opt = ElementLocator(By.XPATH, "//*["
                                                                  "@id='SelectedNewsletterSubscriptionStoreIds_listbox"
                                                                  "']/li[text()='Test store "
                                                                  "2'] ")
        self.__div_customer_role = ElementLocator(By.XPATH, "(//div[@class='k-multiselect-wrap k-floatwrap'])[2]")
        self.__li_administrators_role_opt = ElementLocator(By.XPATH, "//*[@id='SelectedCustomerRoleIds_listbox']/li[text("
                                                              ")='Administrators']")
        self.__select_vendor_id = ElementLocator(By.ID, "VendorId")
        self.__checkbox_active = ElementLocator(By.ID, "Active")
        self.__textarea_admin_comment = ElementLocator(By.ID, "AdminComment")
        self.__btn_save = ElementLocator(By.NAME, "save")
        self.__btn_save_continue = ElementLocator(By.NAME, "save-continue")

    @property
    def textbox_email(self):
        return self.driver.find_element(self.__textbox_email.by, self.__textbox_email.value)

    @property
    def textbox_password(self):
        return self.driver.find_element(self.__textbox_password.by, self.__textbox_password.value)

    @property
    def textbox_first_name(self):
        return self.driver.find_element(self.__textbox_first_name.by, self.__textbox_first_name.value)

    @property
    def textbox_last_name(self):
        return self.driver.find_element(self.__textbox_last_name.by, self.__textbox_last_name.value)

    @property
    def textbox_gender_male(self):
        return self.driver.find_element(self.__textbox_gender_male.by, self.__textbox_gender_male.value)

    @property
    def textbox_gender_female(self):
        return self.driver.find_element(self.__textbox_gender_female.by, self.__textbox_gender_female.value)

    @property
    def textbox_dateOfBirth(self):
        return self.driver.find_element(self.__textbox_dateofbirth.by, self.__textbox_dateofbirth.value)

    @property
    def textbox_company(self):
        return self.driver.find_element(self.__textbox_company.by, self.__textbox_company.value)

    @property
    def checkbox_taxExempt(self):
        return self.driver.find_element(self.__checkbox_taxexempt.by, self.__checkbox_taxexempt.value)

    @property
    def div_newsletter(self):
        return self.driver.find_element(self.__div_newsletter.by, self.__div_newsletter.value)

    @property
    def li_newsletter_test_store_2_opt(self):
        return self.driver.find_element(
            self.__li_newsletter_test_store_2_opt.by, self.__li_newsletter_test_store_2_opt.value)

    @property
    def div_customer_role(self):
        return self.driver.find_element(self.__div_customer_role.by, self.__div_customer_role.value)

    @property
    def li_Administrators_role_opt(self):
        return self.driver.find_element(self.__li_administrators_role_opt.by, self.__li_administrators_role_opt.value)

    @property
    def select_vendor_id(self):
        return self.driver.find_element(self.__select_vendor_id.by, self.__select_vendor_id.value)

    @property
    def checkbox_active(self):
        return self.driver.find_element(self.__checkbox_active.by, self.__checkbox_active.value)

    @property
    def textarea_admin_comment(self):
        return self.driver.find_element(self.__textarea_admin_comment.by, self.__textarea_admin_comment.value)

    @property
    def btn_save(self):
        return self.driver.find_element(self.__btn_save.by, self.__btn_save.value)

    @property
    def btn_save_continue(self):
        return self.driver.find_element(self.__btn_save_continue.by, self.__btn_save_continue.value)


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
