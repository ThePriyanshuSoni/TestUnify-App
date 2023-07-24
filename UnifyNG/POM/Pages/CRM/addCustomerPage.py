from selenium.webdriver.common.by import By
from UnifyNG.POM.Locators.Locators import Locators

class AddCustomerPage():

    def __init__(self, driver):
        self.driver = driver
        self.crm_customerid_textbox_id = "crmCustomerId"
        self.firstname_textbox_id      = "firstName"
        self.lastname_textbox_id       = "lastName"
        self.biller_dropdown_id        = "billerId"
        self.labels_dropdown_id        = "tags"
        self.notes_textbox_id          = "notes"
        self.email_textbox_id          = "email"
        self.mobile_textbox_id         = "phoneNo"
        self.name_textbox_id           = "fullName"
        self.addressline_textbox_id    = "addressLine"
        self.landmark_textbox_id       = "landmark"
        self.pincode_textbox_id        = "pincode"
        self.city_textbox_id           = "city"
        self.country_textbox_id        = "country"
        self.india_drop_select_xpath   = "//li[102]"
        self.state_textbox_id          = "state"
        self.up_drop_select_xpath      = "//li[normalize-space()='Uttar Pradesh']"
        self.comment_textbox_id        = "6486f58f3dca617e7fcabaa5"

    def enter_customerid(self, customerId):
        self.driver.find_element(By.ID, self.crm_customerid_textbox_id).clear()
        self.driver.find_element(By.ID, self.crm_customerid_textbox_id).send_keys(customerId)

    def enter_firstname(self, firstname):
        self.driver.find_element(By.ID, self.firstname_textbox_id).send_keys(firstname)

    def enter_lastname(self, lastname):
        self.driver.find_element(By.ID, self.lastname_textbox_id).send_keys(lastname)

