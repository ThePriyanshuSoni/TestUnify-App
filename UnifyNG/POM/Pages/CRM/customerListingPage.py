from selenium.webdriver.common.by import By
from UnifyNG.POM.Locators.Locators import Locators


class CustomerListingPage():

    def __int__(self, driver):
        self.driver = driver

        # self.click_add_new_xpath = "//button[normalize-space()='Add New']"

    # def click_add_new(self):
    #     self.driver.find_element(By.XPATH, self.click_add_new_xpath).click()
