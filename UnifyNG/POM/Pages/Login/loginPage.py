from selenium.webdriver.common.by import By
from UnifyNG.POM.Locators.Locators import Locators


class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.tenantName_textbox_id = Locators.tenantName_textbox_id
        self.continue_button_xpath = Locators.continue_button_xpath
        self.username_textbox_id   = Locators.username_textbox_id
        self.password_textbox_id   = Locators.password_textbox_id
        self.tenantLogin_Button_id = Locators.tenantLogin_Button_id
        self.invalidUsername_message_xpath = "//span[@id='input-error']"
        self.new_password_id = "password-new"
        self.confirm_password_id = "password-new"
        self.submit_button_xpath = "//input[@value='Submit']"

    def enter_tenant(self, tenantName):
        self.driver.find_element(By.ID, self.tenantName_textbox_id).clear()
        self.driver.find_element(By.ID, self.tenantName_textbox_id).send_keys(tenantName)

    def click_continue(self):
        self.driver.find_element(By.XPATH, self.continue_button_xpath).click()

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.username_textbox_id).clear()
        self.driver.find_element(By.ID, self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_textbox_id).clear()
        self.driver.find_element(By.ID, self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, self.tenantLogin_Button_id).click()

    def check_invalid_username_message(self, message):
        msg = self.driver.find_element(By.XPATH, self.invalidUsername_message_xpath).text
        return msg

    def enter_new_password(self, new):
        self.driver.find_element(By.ID, self.new_password_id).send_keys(new)

    def enter_confirm_password(self, confirm):
        self.driver.find_element(By.ID, self.confirm_password_id).send_keys(confirm)

    def click_submit(self):
        self.driver.find_element(By.XPATH, self.submit_button_xpath).click()