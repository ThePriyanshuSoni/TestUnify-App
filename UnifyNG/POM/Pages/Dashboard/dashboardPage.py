from selenium.webdriver.common.by import By
from UnifyNG.POM.Locators.Locators import Locators


class DashboardPage():

    def __init__(self, driver):
        self.driver = driver

        self.click_crm_management_xpath   = "//span[normalize-space()='CRM Management']"
        self.click_customers_xpath        = "//span[normalize-space()='Customers']"
        self.account_link_xpath           = Locators.account_link_xpath
        self.account_logout_xpath         = Locators.account_logout_xpath
        self.click_add_new_xpath          = "//button[normalize-space()='Add New']"
        self.click_settings_xpath         = "//span[normalize-space()='Settings']"
        self.click_site_settings_xpath    = "//span[normalize-space()='Site Settings']"
        self.click_business_profile_xpath = "//span[normalize-space()='Business Profile']"
        self.click_billing_frequency_xpath= "//span[normalize-space()='Billing Frequency']"

    def click_account(self):
        self.driver.find_element(By.XPATH, self.account_link_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.account_logout_xpath).click()

    def click_crm(self):
        self.driver.find_element(By.XPATH, self.click_crm_management_xpath).click()

    def click_customers(self):
        self.driver.find_element(By.XPATH, self.click_customers_xpath).click()

    def click_add_new(self):
        self.driver.find_element(By.XPATH, self.click_add_new_xpath).click()

    def click_settings(self):
        self.driver.find_element(By.XPATH, self.click_settings_xpath).click()

    def click_site_settings(self):
        self.driver.find_element(By.XPATH, self.click_site_settings_xpath).click()

    def click_business_profile(self):
        self.driver.find_element(By.XPATH, self.click_business_profile_xpath).click()

    def click_billing_frequency(self):
        self.driver.find_element(By.XPATH, self.click_billing_frequency_xpath).click()
