from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from UnifyNG.POM.Locators.Locators import Locators


class AddBusinessProfilePage():

    def __init__(self, driver):
        self.driver = driver

        self.add_b_profile_xpath   = "//button[normalize-space()='Add Business Profile']"
        self.businessname_textbox_xpath  = "//input[@id='businessName']"
        self.cin_number_textbox_id       = "cinNumber"
        self.address_textbox_id          = "address"
        self.country_dropdown_id         = "Country"
        self.india_drop_select_xpath     = "//div[@id='menu-country']//li[102]"
        self.state_dropdown_id           = "state"
        self.up_drop_select_xpath        = "//li[normalize-space()='Uttar Pradesh']"
        self.city_textbox_id             = "city"
        self.pincode_textbox_id          = "pincode"
        self.phonenumber_textbox_id      = "phoneNumber"
        self.emailid_textbox_id          = "emailId"
        self.website_textbox_id          = "website"
        self.timezone_dropdown_id        = "timeZone"
        self.kolkata_drop_select_xpath   = "//li[normalize-space()='(UTC+05:30) Chennai, Kolkata, Mumbai, New Delhi']"
        self.save_button_xpath           = "//button[normalize-space()='Save']"

    def click_add_bussiness_profile(self):
        self.driver.find_element(By.XPATH, self.add_b_profile_xpath).click()

    def enter_businessname(self, business):
        self.driver.find_element(By.XPATH, self.businessname_textbox_xpath).send_keys(business)

    def enter_cin_number(self, cin):
        self.driver.find_element(By.ID, self.cin_number_textbox_id).send_keys(cin)

    def enter_address(self, address):
        self.driver.find_element(By.ID, self.address_textbox_id).send_keys(address)

    def click_country(self):
        self.driver.find_element(By.ID, self.country_dropdown_id).click()

    def select_country(self):
        self.driver.find_element(By.XPATH, self.india_drop_select_xpath).click()

    def click_state(self):
        self.driver.find_element(By.ID, self.state_dropdown_id).click()

    def select_state(self):
        self.driver.find_element(By.XPATH, self.up_drop_select_xpath).click()

    def enter_city(self, city):
        self.driver.find_element(By.ID, self.city_textbox_id).send_keys(city)

    def enter_pincode(self, pincode):
        self.driver.find_element(By.ID, self.pincode_textbox_id).send_keys(pincode)

    def enter_phone(self, phoneNo):
        self.driver.find_element(By.ID, self.phonenumber_textbox_id).send_keys(phoneNo)

    def enter_email(self, email):
        self.driver.find_element(By.ID, self.emailid_textbox_id).send_keys(email)

    def enter_website(self, website):
        self.driver.find_element(By.ID, self.website_textbox_id).send_keys(website)

    def click_timezone(self):
        self.driver.find_element(By.ID, self.timezone_dropdown_id).click()

    def select_kolkata(self):
        self.driver.find_element(By.XPATH, self.kolkata_drop_select_xpath).click()

    def click_save(self):
        self.driver.find_element(By.XPATH, self.save_button_xpath).click()
        