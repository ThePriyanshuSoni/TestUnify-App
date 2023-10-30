import HtmlTestRunner
from selenium import webdriver
import time

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import unittest
from UnifyNG.POM.Pages.Login.loginPage import LoginPage
from UnifyNG.POM.Pages.Dashboard.dashboardPage import DashboardPage


class LoginTest(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

        # cls.chrome_options = Options()
        # cls.chrome_options.add_argument('--headless')
        # cls.driver = webdriver.Chrome(options=chrome_options)
        # cls.driver.implicitly_wait(10)
        # cls.driver.maximize_window()


    def test_01_valid_login(self):
        driver = self.driver
        driver.get("http://testunifyng.inventum.co/login")

        login = LoginPage(driver)
        login.enter_tenant("ketan")
        login.enter_continue()
        login.enter_username("ketan")
        login.enter_password("password")
        login.click_login()

        dashboard = DashboardPage(driver)
        time.sleep(2)
        dashboard.click_account()
        time.sleep(2)
        dashboard.click_logout()
        time.sleep(2)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("login Test Pass")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/home/priyansu/Desktop/testing/unifyng-automation-testing/UnifyNG/Reports"))