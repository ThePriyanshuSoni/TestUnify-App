from selenium.webdriver.common.by import By
from UnifyNG.POM.Locators.Locators import Locators


class DashboardPage():

    def __init__(self, driver):
        self.driver = driver

        #CRM
        self.crm_management_xpath   = "//span[normalize-space()='CRM Management']"
        self.customers_xpath        = "//span[normalize-space()='Customers']"

        #NgCreator
        self.ng_creator_xpath       = "//span[normalize-space()='NgCreator']"

        self.account_link_xpath     = Locators.account_link_xpath
        self.account_logout_xpath   = Locators.account_logout_xpath
        self.add_new_xpath          = "//button[normalize-space()='Add New']"
        self.settings_xpath         = "//span[normalize-space()='Settings']"
        self.site_settings_xpath    = "//span[normalize-space()='Site Settings']"
        self.business_profile_xpath = "//span[normalize-space()='Business Profile']"
        self.billing_frequency_xpath= "//span[normalize-space()='Billing Frequency']"
        self.billing_cycle_xpath    = "//span[normalize-space()='Billing Cycle']"
        self.subscriptions_xpath    = "//span[normalize-space()='Subscription']"
        #Product Catalogs
        self.product_catalogs_xpath  = "//span[normalize-space()='Product Catalogs']"
        self.product_families_xpath  = "//span[normalize-space()='Product Families']"
        self.product_xpath           = "//span[normalize-space()='Product']"
        self.price_book_xpath        = "//span[normalize-space()='Price Book']"
        #Tax Profile
        self.tax_configuration_xpath = "//span[normalize-space()='Tax Configuration']"




    def click_account(self):
        self.driver.find_element(By.XPATH, self.account_link_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.account_logout_xpath).click()

    def click_crm(self):
        self.driver.find_element(By.XPATH, self.crm_management_xpath).click()

    def click_customers(self):
        self.driver.find_element(By.XPATH, self.customers_xpath).click()

    def click_add_new(self):
        self.driver.find_element(By.XPATH, self.add_new_xpath).click()

    def click_settings(self):
        self.driver.find_element(By.XPATH, self.settings_xpath).click()

    def click_site_settings(self):
        self.driver.find_element(By.XPATH, self.site_settings_xpath).click()

    def click_business_profile(self):
        self.driver.find_element(By.XPATH, self.business_profile_xpath).click()

    def click_billing_frequency(self):
        self.driver.find_element(By.XPATH, self.billing_frequency_xpath).click()

    def click_billing_cycle(self):
        self.driver.find_element(By.XPATH, self.billing_cycle_xpath).click()

    def click_subscriptions(self):
        self.driver.find_element(By.XPATH, self.subscriptions_xpath).click()

    def click_product_catalogs(self):
        self.driver.find_element(By.XPATH, self.product_catalogs_xpath).click()

    def click_product_families(self):
        self.driver.find_element(By.XPATH, self.product_families_xpath).click()

    def click_product(self):
        self.driver.find_element(By.XPATH, self.product_xpath).click()

    def click_price_book(self):
        self.driver.find_element(By.XPATH, self.price_book_xpath).click()

    def page_scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0);")

    def page_scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def click_tax_configuration(self):
        self.driver.find_element(By.XPATH, self.tax_configuration_xpath).click()

    def click_ng_creator(self):
        self.driver.find_element(By.XPATH, self.ng_creator_xpath).click()

