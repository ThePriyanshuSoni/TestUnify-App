from selenium import webdriver
import time
import unittest
from UnifyNG.POM.Pages.Login.loginPage import LoginPage
from UnifyNG.POM.Pages.Dashboard.dashboardPage import DashboardPage
from UnifyNG.POM.Pages.Settings.SiteSettings.BillingFrequency.addBillingFrequencyPage import AddBillingFrequencyPage




class TestAddBillingFrequency(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    def test_01_valid_frequency(self):
        driver = self.driver
        driver.get("http://unifyng.inventum.co/login")

        login = LoginPage(driver)
        login.enter_tenant("priyanshu")
        login.enter_continue()
        login.enter_username("priyanshu")
        login.enter_password("password")
        login.click_login()
        time.sleep(2)

        dashboard = DashboardPage(driver)
        dashboard.click_settings()
        dashboard.click_site_settings()
        dashboard.click_billing_frequency()

        freq = AddBillingFrequencyPage(driver)
        freq.click_add_new()
        freq.enter_frequency_name("Priyanshu")
        freq.click_billing_frequency()
        freq.select_week()
        freq.enter_count("34")
        freq.click_save()




        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print(">>> Billing Frequency Added Successfully.")