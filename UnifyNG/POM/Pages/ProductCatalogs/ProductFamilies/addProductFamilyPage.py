from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from UnifyNG.POM.Locators.Locators import Locators


class AddProductFamilyPage():

    def __init__(self, driver):
        self.driver = driver

        self.add_product_family_xpath       = "//button[normalize-space()='Add Product Family']"
        self.product_family_name_textbox_id = "product_family_name"
        self.family_description_textbox_id  = "description"
        self.save_button_xpath              = "//button[normalize-space()='Save']"

    def click_add_product_family(self):
        self.driver.find_element(By.XPATH, self.add_product_family_xpath).click()

    def enter_product_family_name(self, family_name):
        self.driver.find_element(By.ID, self.product_family_name_textbox_id).send_keys(family_name)

    def enter_description(self, description):
        self.driver.find_element(By.ID, self.family_description_textbox_id).send_keys(description)

    def click_save(self):
        self.driver.find_element(By.XPATH, self.save_button_xpath).click()
