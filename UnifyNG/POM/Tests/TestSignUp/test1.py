import HtmlTestRunner
from faker import Faker
from selenium import webdriver
import time

from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import unittest
from UnifyNG.POM.Pages.Login.loginPage import LoginPage
from UnifyNG.POM.Pages.Signup.signupPage import SignupPage
from UnifyNG.POM.Pages.Dashboard.dashboardPage import DashboardPage

fake = Faker(['en_US'])
fake_word = fake.word()
fake_name = fake.user_name()
streetName = fake.street_name()
num = fake.random_int(min=1, max=100)


class LoginTest(unittest.TestCase):
    base_dev_url = "https://unifyng.inventum.co/login"
    priyanshu_tenant = "https://priyanshu.inventum.co/"


    @classmethod
    def setUp(cls):
        # cls.driver = webdriver.Chrome()
        # cls.driver.implicitly_wait(10)
        # cls.driver.maximize_window()

        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    def test_001_tenant(self):
        driver = self.driver
        driver.get(self.base_dev_url)

        print("Test Pass Bro")



    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()


# if __name__ == "__main__":
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/home/priyansu/Desktop/testing/unifyng-automation-testing/UnifyNG/Reports"))