from selenium.webdriver.common.by import By



class AddBillingFrequencyPage():

    def __init__(self, driver):
        self.driver = driver

        self.add_biller_button_xpath  = "//button[normalize-space()='Add New']"
        self.freq_name_textbox_id     = "billingFrequencyName"
        self.frequency_dropdown_id    = "temporal_uom"
        self.week_drop_select_xpath   = "//li[normalize-space()='WEEK']"
        self.frequency_count_id       = "billingFrequencyCount"
        self.save_button_xpath        = "//button[normalize-space()='Save']"

    def click_add_new(self):
        self.driver.find_element(By.XPATH, self.add_biller_button_xpath).click()

    def enter_frequency_name(self, freq):
        self.driver.find_element(By.ID, self.freq_name_textbox_id).send_keys("Test")

    def click_billing_frequency(self):
        self.driver.find_element(By.ID, self.frequency_dropdown_id).click()

    def select_week(self):
        self.driver.find_element(By.XPATH, self.week_drop_select_xpath).click()

    def enter_count(self, count):
        self.driver.find_element(By.ID, self.frequency_count_id).send_keys(count)

    def click_save(self):
        self.driver.find_element(By.XPATH, self.save_button_xpath).click()
