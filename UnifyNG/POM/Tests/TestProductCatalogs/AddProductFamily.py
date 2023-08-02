from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
from UnifyNG.POM.Pages.Login.loginPage import LoginPage
from UnifyNG.POM.Pages.Dashboard.dashboardPage import DashboardPage
from UnifyNG.POM.Pages.ProductCatalogs.ProductFamilies.addProductFamilyPage import AddProductFamilyPage


class AddProductFamily(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    def test_01_valid_add_product_family(self):
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
        dashboard.click_product_catalogs()
        dashboard.click_product_families()
        time.sleep(2)

        family = AddProductFamilyPage(driver)
        family.click_add_product_family()
        family.enter_product_family_name("Priyanshu")
        family.enter_description("Hello there Priyanshu Here!")
        family.click_save()


        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print(" Product Family Added Successfully.")

