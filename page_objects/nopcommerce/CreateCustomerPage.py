from seleniumpagefactory.Pagefactory import PageFactory


class CreateCustomer(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        "textbox_email": ("ID", "Email"),
        "textbox_password": ("ID", "Password"),
        "textbox_first_name": ("ID", "FirstName"),
        "textbox_last_name": ("ID", "LastName"),
        "textbox_gender_male": ("ID", "Gender_Male"),
        "textbox_gender_female": ("ID", "Gender_Female"),
        "textbox_dateOfBirth": ("ID", "DateOfBirth"),
        "textbox_company": ("ID", "Company"),
        "checkbox_taxExempt": ("ID", "IsTaxExempt"),
        "div_newsletter": (
            "XPATH",
            "(//div[@class='k-multiselect-wrap k-floatwrap'])[1]",
        ),
        "li_newsletter_test_store_2_opt": (
            "XPATH",
            "//*[@id='SelectedNewsletterSubscriptionStoreIds_listbox']/li[text()='Test store 2']",
        ),
        "div_customer_role": (
            "XPATH",
            "(//div[@class='k-multiselect-wrap k-floatwrap'])[2]",
        ),
        "li_Administrators_role_opt": (
            "XPATH",
            "//*[@id='SelectedCustomerRoleIds_listbox']/li[text()='Administrators']",
        ),
        "select_vendor_id": ("ID", "VendorId"),
        "checkbox_active": ("ID", "Active"),
        "textarea_admin_comment": ("ID", "AdminComment"),
        "btn_save": ("NAME", "save"),
        "btn_save_continue": ("NAME", "save-continue"),
    }


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
