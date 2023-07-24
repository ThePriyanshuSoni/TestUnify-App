from selenium.webdriver.common.by import By
from UnifyNG.POM.Locators.Locators import Locators


class DashboardPage():

    def __init__(self, driver):
        self.driver = driver

        self.click_crm_management_xpath = "//span[normalize-space()='CRM Management']"
        self.click_customers_xpath      = "//span[normalize-space()='Customers']"
        self.account_link_xpath         = Locators.account_link_xpath
        self.account_logout_xpath       = Locators.account_logout_xpath


    def click_account(self):
        self.driver.find_element(By.XPATH, self.account_link_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.account_logout_xpath).click()

    def click_crm(self):
        self.driver.find_element(By.XPATH, self.click_crm_management_xpath).click()

    def click_customers(self):
        self.driver.find_element(By.XPATH, self.click_customers_xpath).click()
