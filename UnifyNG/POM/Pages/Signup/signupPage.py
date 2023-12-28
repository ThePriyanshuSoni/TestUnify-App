from selenium.webdriver.common.by import By
from UnifyNG.POM.Locators.Locators import Locators


class SignupPage():

    def __init__(self, driver):
        self.driver = driver

        self.tenant_signup_button_xpath = "//a[normalize-space()='SignUp?']"
        self.silver_plan_button_xpath = "//div[@class='MuiBox-root css-51xexg']//div[1]//div[1]//div[8]//button[1]"
        self.email_textbox_id = "email"
        self.continue_button_xpath = "//button[normalize-space()='Continue']"
        self.firstname_textbox_id = "first_name"
        self.lastname_textbox_id = "last_name"
        self.mobile_no_textbox_id = "mobile_no"
        self.organisation_textbox_id = "organisation_name"
        self.city_textbox_id = "city"
        self.state_textbox_id = "state"
        self.country_textbox_id = "country"
        self.pincode_textbox_id = "pincode"
        self.shipping_add_textbox_id = "shipping_address"
        self.billing_add_textbox_id = "billing_address"
        self.gstin_textbox_id = "gstin"
        self.city_textbox_id = "city"
        self.city_textbox_id = "city"
        self.upi_qr_button_xpath = "//div[text()='UPI / QR']"
        self.upi_id_button_id = "new-vpa-field-upi"
        self.upi_textbox_id = "vpa-upi"
        self.org_name_textbox_id = "tenant_name"
        self.verify_button_xpath = "//button[normalize-space()='verify']"
        self.login_verify_button_xpath = "//button[normalize-space()='Login']"

    def click_signup(self):
        self.driver.find_element(By.XPATH, self.tenant_signup_button_xpath).click()

    def click_silver_purchase(self):
        self.driver.find_element(By.XPATH, self.silver_plan_button_xpath).click()

    def enter_email(self, email):
        self.driver.find_element(By.ID, self.email_textbox_id).send_keys(email)

    def enter_firstname(self, first):
        self.driver.find_element(By.ID, self.firstname_textbox_id).send_keys(first)

    def enter_lastname(self, last):
        self.driver.find_element(By.ID, self.lastname_textbox_id).send_keys(last)

    def enter_mobile_no(self, mobile):
        self.driver.find_element(By.ID, self.mobile_no_textbox_id).send_keys(mobile)

    def enter_organisation_name(self, organisation):
        self.driver.find_element(By.ID, self.organisation_textbox_id).send_keys(organisation)

    def enter_city(self, city):
        self.driver.find_element(By.ID, self.city_textbox_id).send_keys(city)

    def enter_state(self, state):
        self.driver.find_element(By.ID, self.state_textbox_id).send_keys(state)

    def enter_country(self, country):
        self.driver.find_element(By.ID, self.country_textbox_id).send_keys(country)

    def enter_pincode(self, pin):
        self.driver.find_element(By.ID, self.pincode_textbox_id).send_keys(pin)

    def enter_shipping_add(self, ship):
        self.driver.find_element(By.ID, self.shipping_add_textbox_id).send_keys(ship)

    def enter_billing_add(self, bill):
        self.driver.find_element(By.ID, self.billing_add_textbox_id).send_keys(bill)

    def enter_gst(self, gst):
        self.driver.find_element(By.ID, self.gstin_textbox_id).send_keys(gst)

    def click_continue(self):
        self.driver.find_element(By.XPATH, self.continue_button_xpath).click()

    def click_upi_qr(self):
        self.driver.find_element(By.XPATH, self.upi_qr_button_xpath).click()

    def click_upi_id(self):
        self.driver.find_element(By.ID, self.upi_id_button_id).click()

    def enter_upi_id(self, upi):
        self.driver.find_element(By.ID, self.upi_textbox_id).send_keys(upi)

    def enter_org_name(self, org):
        self.driver.find_element(By.ID, self.org_name_textbox_id).send_keys(org)

    def click_verify_org(self):
        self.driver.find_element(By.XPATH, self.verify_button_xpath).click()

    def click_verify_login(self):
        self.driver.find_element(By.XPATH, self.login_verify_button_xpath).click()

