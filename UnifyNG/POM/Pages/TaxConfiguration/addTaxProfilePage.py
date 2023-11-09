from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from UnifyNG.POM.Locators.Locators import Locators


class AddTaxProfilePage():

    def __init__(self, driver):
        self.driver = driver

        self.add_tax_profile_xpath    = "//button[normalize-space()='Add New']"
        self.profile_name_textbox_id  = "tax_profile_name"
        self.back_button_xpath        = "//button[normalize-space()='Back']"
        self.save_button_xpath        = "//button[normalize-space()='Save']"
        self.discard_button_xpath     = "//button[normalize-space()='Discard']"
        self.settings_icon_xpath      = "/html[1]/body[1]/div[1]/div[2]/div[1]/main[1]/div[3]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[4]/*[name()='svg'][1]"
        self.manual_select_type_radio_xpath = "//input[@value='MANUAL']"
        self.gst_select_type_radio_xpath    = "//input[@value='GST']"
        self.label_textbox_id         = "label"
        self.tax_rate_textbox_id      = "tax_rate"
        self.sgst_textbox_id          = "sgst_ugst"
        self.cgst_textbox_id          = "cgst"


    def click_add_tax_profile(self):
        self.driver.find_element(By.XPATH, self.add_tax_profile_xpath).click()

    def enter_profile_name(self, pname):
        self.driver.find_element(By.ID, self.profile_name_textbox_id).send_keys(pname)

    def click_back(self):
        self.driver.find_element(By.XPATH, self.back_button_xpath).click()

    def click_save(self):
        self.driver.find_element(By.XPATH, self.save_button_xpath).click()

    def click_discard(self):
        self.driver.find_element(By.XPATH, self.discard_button_xpath).click()

    def click_settings_icon(self):
        self.driver.find_element(By.XPATH, self.settings_icon_xpath).click()

    def click_gst_type(self):
        self.driver.find_element(By.XPATH, self.gst_select_type_radio_xpath).click()

    def click_manual_type(self):
        self.driver.find_element(By.XPATH, self.manual_select_type_radio_xpath).click()

    def enter_label(self, label):
        self.driver.find_element(By.ID, self.label_textbox_id).send_keys(label)

    def enter_add_tax_rate(self, rate):
        self.driver.find_element(By.ID, self.tax_rate_textbox_id).send_keys(rate)

    def enter_sgst(self, sgst):
        self.driver.find_element(By.ID, self.sgst_textbox_id).send_keys(sgst)

    def enter_cgst(self, cgst):
        self.driver.find_element(By.ID, self.cgst_textbox_id).send_keys(cgst)


