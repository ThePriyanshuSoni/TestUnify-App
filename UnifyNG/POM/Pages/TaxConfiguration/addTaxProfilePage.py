from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from UnifyNG.POM.Locators.Locators import Locators


class AddTaxProfilePage():

    def __init__(self, driver):
        self.driver = driver

        self.add_tax_profile_xpath    = "//button[normalize-space()='Add New']"
        self.profile_name_textbox_id  = "tax_profile_name"
        self.save_button_xpath        = "//button[normalize-space()='Save']"
        self.discard_button_xpath     = "//button[normalize-space()='Discard']"




    def click_add_tax_profile(self):
        self.driver.find_element(By.XPATH, self.add_tax_profile_xpath).click()

    def enter_profile_name(self, pname):
        self.driver.find_element(By.ID, self.profile_name_textbox_id).send_keys(pname)

    def click_save(self):
        self.driver.find_element(By.XPATH, self.save_button_xpath).click()

    def click_discard(self):
        self.driver.find_element(By.XPATH, self.discard_button_xpath).click()