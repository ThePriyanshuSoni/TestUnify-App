from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
from UnifyNG.POM.Pages.Login.loginPage import LoginPage
from UnifyNG.POM.Pages.Dashboard.dashboardPage import DashboardPage
from UnifyNG.POM.Pages.Settings.SiteSettings.BussinessProfile.addBillerPagePage import AddBillerPage




class TestAddBiller(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    def test_01_valid_add_biller(self):
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
        time.sleep(2)

        biller = AddBillerPage(driver)
        biller.click_add_biller()
        biller.enter_billername("Priyanshu")
        biller.enter_address("MG Trendz, Vapi Road")
        biller.click_country()
        biller.select_country()
        biller.click_state()
        time.sleep(2)
        biller.select_state()
        biller.enter_city("Kanpur")
        biller.enter_pincode("208017")
        biller.enter_phone("9122439011")
        biller.enter_email("testing@inventum.net")
        biller.enter_website("https://google.com")
        biller.click_save()



        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print(" Biller Added Successfully.")

