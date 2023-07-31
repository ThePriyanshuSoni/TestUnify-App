from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from UnifyNG.POM.Locators.Locators import Locators


class AddBillerPage():

    def __init__(self, driver):
        self.driver = driver
        self.add_biller_button_xpath  = "//button[normalize-space()='Add Biller']"
        self.billername_textbox_id    = "billerName"
        self.address_textbox_id       = "address"
        self.country_dropdown_id      = "Country"
        self.india_drop_select_xpath  = "//div[@id='menu-country']//li[102]"
        self.state_dropdown_id        = "State"
        self.up_drop_select_xpath     = "//li[normalize-space()='Uttar Pradesh']"
        self.city_textbox_id          = "city"
        self.pincode_textbox_id       = "pincode"
        self.phonenumber_textbox_id   = "phoneNumber"
        self.emailid_textbox_id       = "emailId"
        self.website_textbox_id       = "website"
        self.save_button_xpath        = "//button[normalize-space()='Save']"



    def click_add_biller(self):
        self.driver.find_element(By.XPATH, self.add_biller_button_xpath).click()

    def enter_billername(self, billname):
        self.driver.find_element(By.ID, self.billername_textbox_id).send_keys(billname)

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

    def click_save(self):
        self.driver.find_element(By.XPATH, self.save_button_xpath).click()