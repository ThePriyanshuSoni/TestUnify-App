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
        self.action_three_dot_button_xpath  = "/html[1]/body[1]/div[1]/div[2]/div[1]/main[1]/div[3]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/button[1]/*[name()='svg'][1]"
        self.dot_edit_xpath                = "//li[normalize-space()='Edit']"
        self.dot_delete_xpath              = "//li[normalize-space()='Delete']"
        self.delete_product_name_textbox_id = "product_name"
        self.delete_about_to_delete_button_xpath = "//button[normalize-space()='You are about to delete product']"


    def click_add_product_family(self):
        self.driver.find_element(By.XPATH, self.add_product_family_xpath).click()

    def enter_product_family_name(self, family_name):
        self.driver.find_element(By.ID, self.product_family_name_textbox_id).send_keys(family_name)

    def enter_description(self, description):
        self.driver.find_element(By.ID, self.family_description_textbox_id).send_keys(description)

    def click_save(self):
        self.driver.find_element(By.XPATH, self.save_button_xpath).click()

    def click_action_three_dot(self):
        self.driver.find_element(By.XPATH, self.action_three_dot_button_xpath).click()

    def click_action_edit(self):
        self.driver.find_element(By.XPATH, self.dot_edit_xpath).click()

    def click_action_delete(self):
        self.driver.find_element(By.XPATH, self.dot_delete_xpath).click()

    def enter_delete_product_name(self, d1):
        self.driver.find_element(By.ID, self.delete_product_name_textbox_id).send_keys(d1)

    def click_are_you_about_to_delete(self):
        self.driver.find_element(By.XPATH, self.delete_about_to_delete_button_xpath).click()

