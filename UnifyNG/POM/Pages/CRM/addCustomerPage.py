from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from UnifyNG.POM.Locators.Locators import Locators


class AddCustomerPage():

    def __init__(self, driver):
        self.driver = driver

        self.crm_customerid_textbox_id = Locators.crm_customerid_textbox_id
        self.firstname_textbox_id      = Locators.firstname_textbox_id
        self.lastname_textbox_id       = Locators.lastname_textbox_id
        self.biller_dropdown_id        = Locators.biller_dropdown_id
        self.select_biller_xpath       = Locators.select_biller_xpath
        self.label_dropdown_id         = Locators.label_dropdown_id
        self.notes_textbox_id          = Locators.notes_textbox_id
        self.services_dropdown_id      = Locators.services_dropdown_id
        self.internet_drop_select_xpath= Locators.internet_drop_select_xpath
        self.email_textbox_id          = Locators.email_textbox_id
        self.mobile_textbox_id         = Locators.mobile_textbox_id
        self.name_textbox_id           = Locators.name_textbox_id
        self.addressline_textbox_id    = Locators.addressline_textbox_id
        self.landmark_textbox_id       = Locators.landmark_textbox_id
        self.pincode_textbox_id        = Locators.pincode_textbox_id
        self.city_textbox_id           = Locators.city_textbox_id
        self.country_dropdown_id       = Locators.country_dropdown_id
        self.india_drop_select_xpath   = Locators.india_drop_select_xpath
        self.state_dropdown_id         = Locators.state_dropdown_id
        self.up_drop_select_xpath      = Locators.up_drop_select_xpath
        self.comment_textbox_id        = Locators.comment_textbox_id
        self.save_button_xpath         = Locators.save_button_xpath

    def enter_customerid(self, customerId):
        self.driver.find_element(By.ID, self.crm_customerid_textbox_id).clear()
        self.driver.find_element(By.ID, self.crm_customerid_textbox_id).send_keys(customerId)

    def enter_firstname(self, firstname):
        self.driver.find_element(By.ID, self.firstname_textbox_id).send_keys(firstname)

    def enter_lastname(self, lastname):
        self.driver.find_element(By.ID, self.lastname_textbox_id).send_keys(lastname)

    def click_biller(self):
        self.driver.find_element(By.ID, self.biller_dropdown_id).click()

    def select_biller(self):
        self.driver.find_element(By.XPATH, self.select_biller_xpath).click()

    def click_label(self):
        self.driver.find_element(By.ID, self.label_dropdown_id).click()

    def select_label(self, KeyboardKeys1, KeyBoardKeys2):
        self.driver.find_element(By.ID, self.label_dropdown_id).send_keys(KeyboardKeys1, KeyBoardKeys2)

    def enter_notes(self, notes):
        self.driver.find_element(By.ID, self.notes_textbox_id).send_keys(notes)

    def enter_email(self, email):
        self.driver.find_element(By.ID, self.email_textbox_id).send_keys(email)

    def enter_mobile(self, phoneNo):
        self.driver.find_element(By.ID, self.mobile_textbox_id).send_keys(phoneNo)

    def enter_name(self, fullName):
        self.driver.find_element(By.ID, self.name_textbox_id).send_keys(fullName)

    def enter_address_line(self, addressLine):
        self.driver.find_element(By.ID, self.addressline_textbox_id).send_keys(addressLine)

    def enter_landmark(self, landmark):
        self.driver.find_element(By.ID, self.landmark_textbox_id).send_keys(landmark)

    def enter_pincode(self, pincode):
        self.driver.find_element(By.ID, self.pincode_textbox_id).send_keys(pincode)

    def enter_city(self, city):
        self.driver.find_element(By.ID, self.city_textbox_id).send_keys(city)

    def click_country(self):
        self.driver.find_element(By.ID, self.country_dropdown_id).click()

    def select_country(self):
        self.driver.find_element(By.XPATH, self.india_drop_select_xpath).click()

    def click_state(self):
        self.driver.find_element(By.ID, self.state_dropdown_id).click()

    def select_state(self):
        self.driver.find_element(By.XPATH, self.up_drop_select_xpath).click()

    def enter_comment(self, comment):
        self.driver.find_element(By.ID, self.comment_textbox_id).send_keys(comment)

    def click_save(self):
        self.driver.find_element(By.XPATH, self.save_button_xpath).click()
