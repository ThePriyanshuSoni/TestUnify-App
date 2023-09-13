from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import string
import unittest
from UnifyNG.POM.Pages.Login.loginPage import LoginPage
from UnifyNG.POM.Pages.Dashboard.dashboardPage import DashboardPage
from UnifyNG.POM.Pages.Settings.SiteSettings.BussinessProfile.addBusinessProfilePage import AddBusinessProfilePage




class TestAddBusinessProfile(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    def test_01_valid_create(self):
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
        dashboard.click_business_profile()


        profile = AddBusinessProfilePage(driver)
        profile.click_add_bussiness_profile()
        profile.enter_businessname(randomName)
        profile.enter_cin_number(randomStrUpper)
        profile.enter_address("TG1 Xerex, MG Road-1")
        profile.click_country()
        profile.select_country()
        profile.click_state()
        time.sleep(2)
        profile.select_state()
        profile.enter_city("Noida")
        profile.enter_pincode("201301")
        profile.enter_phone(randomMobile)
        profile.enter_email("priyanshu@inventum.in")
        profile.enter_website("http://priyanshu.inventum.co")
        profile.click_timezone()
        profile.select_kolkata()
        profile.click_save()


        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print(" Business Profile Created Successfully.")



if __name__ == "__main__":
    unittest.main()

n = 7
m = 10
name = ''.join(random.choices(string.ascii_lowercase, k=n))
randomName = str(name)
randomMobile = ''.join(random.choices(string.octdigits, k=m))
randomStrUpper = ''.join(random.choices(string.ascii_uppercase + string.digits, k=n))