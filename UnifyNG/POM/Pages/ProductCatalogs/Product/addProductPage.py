from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from UnifyNG.POM.Locators.Locators import Locators


class AddProductPage():

    def __init__(self, driver):
        self.driver = driver

        self.add_product_xpath              = "//button[normalize-space()='Add Product']"
        self.product_family_dropdown_id     = "product_family_ref_id"
        self.product_drop_select_xpath      = "//div[@id='menu-product_family_ref_id']//li[1]"
        self.product_name_textbox_id        = "product_name"
        self.product_description_textbox_id = "product_desc"
        self.most_recept_usage_radio_xpath  = "//input[@value='most_recent_usage']"
        self.webhook_toggle_button_xpath    = "//input[@name='webhook_enabled']"
        self.save_button_xpath              = "//button[normalize-space()='Save']"

    def click_add_product(self):
        self.driver.find_element(By.XPATH, self.add_product_xpath).click()

    def click_product_family(self):
        self.driver.find_element(By.ID, self.product_family_dropdown_id).click()

    def select_product_family(self):
        self.driver.find_element(By.XPATH, self.product_drop_select_xpath).click()

    def enter_product_name(self, name):
        self.driver.find_element(By.ID, self.product_name_textbox_id).send_keys(name)

    def enter_description_name(self, desc):
        self.driver.find_element(By.ID, self.product_description_textbox_id).send_keys(desc)

    def click_radio_recent_usage(self):
        self.driver.find_element(By.XPATH, self.most_recept_usage_radio_xpath).click()

    def click_enable_webhook_toggle(self):
        self.driver.find_element(By.XPATH, self.webhook_toggle_button_xpath).click()

    def click_save_button(self):
        self.driver.find_element(By.XPATH, self.save_button_xpath).click()

