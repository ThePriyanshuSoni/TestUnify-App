from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from UnifyNG.POM.Locators.Locators import Locators


class AddSubscriptionsPage():

    def __init__(self, driver):
        self.driver = driver


        self.add_subscription_xpath   = "//button[normalize-space()='Add Subscription']"

        self.search_filter_textbox_id = "searchText"
        self.frequency_dropdown_id    = "billingFrequency"


        self.fullname_textbox_id      = "fullName"
        self.address_textbox_id       = "addressLine"
        self.landmark_textbox_id      = "landmark"
        self.country_dropdown_id      = "country"
        self.india_drop_select_xpath  = "//li[102]"
        self.state_dropdown_id        = "state"
        self.up_drop_select_xpath     = "//li[normalize-space()='Uttar Pradesh']"
        self.city_textbox_id          = "city"
        self.pincode_textbox_id       = "pincode"





    def click_add_subscription(self):
        self.driver.find_element(By.XPATH, self.add_subscription_xpath).click()

