from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
from UnifyNG.POM.Pages.Login.loginPage import LoginPage
from UnifyNG.POM.Pages.Dashboard.dashboardPage import DashboardPage
from UnifyNG.POM.Pages.ProductCatalogs.Product.addProductPage import AddProductPage


class AddProduct(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    def test_01_valid_add_product(self):
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
        dashboard.click_product()

        product = AddProductPage(driver)
        product.click_add_product()
        product.click_product_family()
        product.select_product_family()
        product.enter_product_name("Priyanshu")
        product.enter_description_name("Hello There Its me :)")
        time.sleep(1)
        product.click_select_service()
        product.select_service()
        product.enter_service_plan_id("64f6eaf4d8319a4fa6014cbe")
        product.click_validate()
        product.click_radio_recent_usage()
        time.sleep(1)
        # product.click_enable_webhook_toggle()
        # time.sleep(2)
        # driver.execute_script("scrollBy(0,300);")
        # time.sleep(5)
        product.click_save_button()

        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print(">>> Product Added Successfully.")


if __name__ == "__main__":
    unittest.main()

