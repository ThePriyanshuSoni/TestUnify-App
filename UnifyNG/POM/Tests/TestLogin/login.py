import HtmlTestRunner
from faker import Faker
from selenium import webdriver
import time

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import unittest
from UnifyNG.POM.Pages.Login.loginPage import LoginPage
from UnifyNG.POM.Pages.Dashboard.dashboardPage import DashboardPage

fake = Faker(['en_US'])
fake_word = fake.word()
fake_name = fake.user_name()
cycleName = fake.street_name()
num = fake.random_int(min=1, max=100)


class LoginTest(unittest.TestCase):
    base_dev_url = "https://unifyng.inventum.co/login"
    priyanshu_tenant = "https://priyanshu.inventum.co/"


    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

        # cls.chrome_options = Options()
        # cls.chrome_options.add_argument('--headless')
        # cls.driver = webdriver.Chrome(options=chrome_options)
        # cls.driver.implicitly_wait(10)
        # cls.driver.maximize_window()


    def test_001_login(self):
        driver = self.driver
        driver.get(self.priyanshu_tenant)

        login = LoginPage(driver)
        # login.enter_tenant("priyanshu")
        # login.click_continue()
        login.enter_username("priyanshu")
        login.enter_password("password")
        login.click_login()
        time.sleep(1)
        actual = driver.title
        expected = "UnifyNG"
        if actual in expected:
            print(f"dashboard Page:> {expected}.")
        else:
            print(f"Invalid Page:> {actual}.")
        time.sleep(1)
        dashboard = DashboardPage(driver)
        time.sleep(2)
        dashboard.click_account()
        time.sleep(2)
        dashboard.click_logout()

    def test_002_login(self):
        driver = self.driver
        driver.get(self.priyanshu_tenant)

        login = LoginPage(driver)
        # login.enter_tenant("priyanshu")
        # login.click_continue()
        login.enter_username("priyanshu")
        login.enter_password(fake_word)
        login.click_login()
        time.sleep(1)
        actual = driver.find_element(By.XPATH, "//span[@id='input-error']").text
        expected = "Invalid username or password."
        if actual in expected:
            print(f" Valid Error:> {expected}.")
        else:
            print(f"Invalid Error:> {actual}.")

    def test_003_login(self):
        driver = self.driver
        driver.get(self.priyanshu_tenant)

        login = LoginPage(driver)
        # login.enter_tenant("priyanshu")
        # login.click_continue()
        login.enter_username("hellotest")
        login.enter_password("password")
        login.click_login()
        time.sleep(1)
        actual = driver.find_element(By.XPATH, "//span[@id='input-error']").text
        expected = "Invalid username or password."
        if actual in expected:
            print(f" Valid Error:> {expected}.")
        else:
            print(f"Invalid Error:> {actual}.")

    def test_004_login(self):
        driver = self.driver
        driver.get(self.priyanshu_tenant)

        login = LoginPage(driver)
        # login.enter_tenant("priyanshu")
        # login.click_continue()
        login.enter_username(fake_word)
        login.enter_password(fake_word)
        login.click_login()
        time.sleep(1)
        actual = driver.find_element(By.XPATH, "//span[@id='input-error']").text
        expected = "Invalid username or password."
        if actual in expected:
            print(f" Valid Error:> {expected}.")
        else:
            print(f"Invalid Error:> {actual}.")


    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/home/priyansu/Desktop/testing/unifyng-automation-testing/UnifyNG/Reports"))