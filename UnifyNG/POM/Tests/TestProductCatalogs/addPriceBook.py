from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
from UnifyNG.POM.Pages.Login.loginPage import LoginPage
from UnifyNG.POM.Pages.Dashboard.dashboardPage import DashboardPage
from UnifyNG.POM.Pages.ProductCatalogs.PriceBook.addPriceBookPage import AddPriceBookPage


class AddPriceBook(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01_valid_add_price_book(self):
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
        dashboard.click_price_book()

        price = AddPriceBookPage(driver)
        time.sleep(3)
        price.click_add_price_book()
        price.enter_price_book_name("Priyanshu")
        price.click_disable_price_toggle()
        time.sleep(2)
        price.click_save_button()
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print(">>> Price Book Added Successfully.")
