from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from UnifyNG.POM.Locators.Locators import Locators


class AddBillingCyclePage():

    def __init__(self, driver):
        self.driver = driver


        self.add_billing_cycle_xpath  = "//button[normalize-space()='Add New']"
        self.b_cyclename_textbox_id   = "billingCycleName"
        self.frequency_dropdown_id    = "billingFrequency"
        self.weekly_drop_select_xpath = "//li[normalize-space()='Weekly']"
        self.billing_date_dropdown_id = "dateOfBilling"
        self.tuesday_drop_select_xpath= "//li[normalize-space()='TUESDAY']"
        self.save_button_xpath        = "//button[normalize-space()='Save']"
        self.toggle_button_xpath      = "//input[@name='enableThisBilling']"
        self.dot_edit_xpath           = "//li[@role='menuitem']"
        self.action_three_dot_button_xpath = "/html[1]/body[1]/div[1]/div[2]/div[1]/main[1]/div[3]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[6]/div[1]/div[1]/button[1]/*[name()='svg'][1]"



    def click_add_billing_cycle(self):
        self.driver.find_element(By.XPATH, self.add_billing_cycle_xpath).click()

    def enter_billing_cycle_name(self, cycle_name):
        self.driver.find_element(By.ID, self.b_cyclename_textbox_id).send_keys(cycle_name)

    def click_billing_frequency(self):
        self.driver.find_element(By.ID, self.frequency_dropdown_id).click()

    def select_billing_frequency(self, bill):
        self.driver.find_element(By.ID, self.frequency_dropdown_id).click(bill)

    def select_weekly(self):
        self.driver.find_element(By.XPATH, self.weekly_drop_select_xpath).click()

    def click_billing_date(self):
        self.driver.find_element(By.ID, self.billing_date_dropdown_id).click()

    def select_tuesday(self):
        self.driver.find_element(By.XPATH, self.tuesday_drop_select_xpath).click()

    def click_save(self):
        self.driver.find_element(By.XPATH, self.save_button_xpath).click()

    def click_enable_toggle_button(self):
        self.driver.find_element(By.XPATH, self.toggle_button_xpath).click()

    def click_action_three_dot(self):
        self.driver.find_element(By.XPATH, self.action_three_dot_button_xpath).click()

    def click_action_edit(self):
        self.driver.find_element(By.XPATH, self.dot_edit_xpath).click()

