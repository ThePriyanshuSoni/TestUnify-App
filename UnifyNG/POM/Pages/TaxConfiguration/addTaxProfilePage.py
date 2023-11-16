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
        self.state_tax_rate_textbox_id= "state_tax_rate"
        self.sgst_textbox_id          = "sgst_ugst"
        self.state_tax_sgst_textbox_id = "state_sgst_ugst"
        self.cgst_textbox_id          = "cgst"
        self.state_tax_cgst_textbox_id = "state_cgst"
        self.cess_textbox_id          = "cess"
        self.state_tax_cess_textbox_id = "state_cess"
        self.add_state_tax_config_button_xpath = "//button[normalize-space()='Add']"
        self.state_tax_biller_dropdown_id         = "state_biller"
        self.state_tax_label_textbox_id        = "state_label"
        self.save_tax_config_button_xpath = "//button[@class='MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium css-1gswqbc-MuiButtonBase-root-MuiButton-root'][normalize-space()='Save']"

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

    def enter_cess(self, cess):
        self.driver.find_element(By.ID, self.cess_textbox_id).send_keys(cess)

    def click_add_state_tax_config(self):
        self.driver.find_element(By.XPATH, self.add_state_tax_config_button_xpath).click()

    def click_state_biller(self):
        self.driver.find_element(By.ID, self.state_tax_biller_dropdown_id).click()

    def select_state_biller(self, k1):
        self.driver.find_element(By.ID, self.state_tax_biller_dropdown_id).send_keys(k1)

    def enter_state_label(self, label):
        self.driver.find_element(By.ID, self.state_tax_label_textbox_id).send_keys(label)

    def enter_state_sgst(self, sgst):
        self.driver.find_element(By.ID, self.state_tax_sgst_textbox_id).send_keys(sgst)

    def enter_state_cgst(self, cgst):
        self.driver.find_element(By.ID, self.state_tax_cgst_textbox_id).send_keys(cgst)

    def enter_state_cess(self, cess):
        self.driver.find_element(By.ID, self.state_tax_cess_textbox_id).send_keys(cess)

    def enter_add_state_tax_rate(self, rate):
        self.driver.find_element(By.ID, self.state_tax_rate_textbox_id).send_keys(rate)

    def click_save_state(self):
        self.driver.find_element(By.XPATH, self.save_tax_config_button_xpath).click()
