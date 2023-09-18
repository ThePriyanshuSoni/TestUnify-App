import HtmlTestRunner
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "../..", ".."))
from UnifyNG.POM.Pages.Login.loginPage import LoginPage
from UnifyNG.POM.Pages.Dashboard.dashboardPage import DashboardPage


class LoginTest(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    def test_01_valid_login(self):
        driver = self.driver
        driver.get("http://unifyng.inventum.co/login")

        login = LoginPage(driver)
        login.enter_tenant("priyanshu")
        login.enter_continue()
        login.enter_username("priyanshu")
        login.enter_password("password")
        login.click_login()

        dashboard = DashboardPage(driver)
        time.sleep(2)
        dashboard.click_account()
        time.sleep(2)
        dashboard.click_logout()
        time.sleep(2)


    def test_02_valid_login(self):
        driver = self.driver
        driver.get("http://unifyng.inventum.co/login")

        login = LoginPage(driver)
        login.enter_tenant("sachin")
        login.enter_continue()
        login.enter_username("sachin")
        login.enter_password("password")
        login.click_login()
        dashboard = DashboardPage(driver)
        time.sleep(2)
        dashboard.click_account()
        time.sleep(2)
        dashboard.click_logout()
        time.sleep(2)


    def test_03_invalid_login(self):
        driver = self.driver
        driver.get("http://unifyng.inventum.co/login")

        login = LoginPage(driver)
        login.enter_tenant("wrongtenant")
        login.enter_continue()
        login.enter_username("sachin")
        login.enter_password("password")
        login.click_login()
        dashboard = DashboardPage(driver)
        time.sleep(2)
        dashboard.click_account()
        time.sleep(2)
        dashboard.click_logout()
        time.sleep(2)

    def test_04_invalid_login(self):
        driver = self.driver
        driver.get("http://unifyng.inventum.co/login")

        login = LoginPage(driver)
        login.enter_tenant("priyanshu")
        login.enter_continue()
        login.enter_username("priyanshus")
        login.enter_password("password")
        login.click_login()
        dashboard = DashboardPage(driver)
        time.sleep(2)
        dashboard.click_account()
        time.sleep(2)
        dashboard.click_logout()
        time.sleep(2)

    def test_05_invalid_login(self):
        driver = self.driver
        driver.get("http://unifyng.inventum.co/login")

        login = LoginPage(driver)
        login.enter_tenant("priyanshu")
        login.enter_continue()
        login.enter_username("priyanshu")
        login.enter_password("passwordss")
        login.click_login()
        dashboard = DashboardPage(driver)
        time.sleep(2)
        dashboard.click_account()
        time.sleep(2)
        dashboard.click_logout()
        time.sleep(2)

    def test_06_invalid_login(self):
        driver = self.driver
        driver.get("http://unifyng.inventum.co/login")

        login = LoginPage(driver)
        login.enter_tenant("priyanshu")
        login.enter_continue()
        login.enter_username("priyansh")
        login.enter_password("passwordss")
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