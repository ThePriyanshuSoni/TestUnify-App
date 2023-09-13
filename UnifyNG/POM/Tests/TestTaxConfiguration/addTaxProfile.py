from selenium import webdriver
import HtmlTestRunner
from selenium.webdriver.common.keys import Keys
import time
import unittest
from UnifyNG.POM.Pages.Login.loginPage import LoginPage
from UnifyNG.POM.Pages.Dashboard.dashboardPage import DashboardPage
from UnifyNG.POM.Pages.TaxConfiguration.addTaxProfilePage import AddTaxProfilePage
import string
import random




class AddTaxProfile(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01_valid_add_tax_profile(self):
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
        dashboard.click_tax_configuration()

        tprofile = AddTaxProfilePage(driver)
        tprofile.click_add_tax_profile()
        tprofile.enter_profile_name(pb)
        tprofile.click_save()

        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print(">>> Tax Profile Created Successfully.")





if __name__ == "__main__":
    unittest.main()

n = 7
name = ''.join(random.choices(string.ascii_uppercase, k=n))
pb = str(name)
