from selenium.webdriver.common.by import By



class AddBillerPage():

    def __init__(self, driver):
        self.driver = driver

        self.add_biller_button_xpath  = "//button[normalize-space()='Add New']"
        self.freq_name_textbox_id