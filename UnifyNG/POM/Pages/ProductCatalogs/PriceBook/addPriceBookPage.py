from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from UnifyNG.POM.Locators.Locators import Locators


class AddPriceBookPage():

    def __init__(self, driver):
        self.driver = driver

        self.add_price_book_xpath           = "//button[normalize-space()='Add Price Book']"
        self.price_book_name_textbox_id     = "price_book_name"
        self.disabled_toggle_button_xpath   = "//div[@class='panel MuiBox-root css-1maxgwy']//input[@name='status']"
        self.save_button_xpath              = "//button[normalize-space()='Save']"

    def click_add_price_book(self):
        self.driver.find_element(By.XPATH, self.add_price_book_xpath).click()

    def enter_price_book_name(self, price):
        self.driver.find_element(By.ID, self.price_book_name_textbox_id).send_keys(price)

    def click_disable_price_toggle(self):
        self.driver.find_element(By.XPATH, self.disabled_toggle_button_xpath).click()

    def click_save_button(self):
        self.driver.find_element(By.XPATH, self.save_button_xpath).click()

