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
        # chrome_options.add_argument('--disable-gpu')
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    def test_001_tenant(self):
        driver = self.driver
        driver.get(self.base_dev_url)

        sign = SignupPage(driver)
        sign.click_signup()
        sign.click_silver_purchase()
        time.sleep(2)
        sign.enter_email("newii@inventum.net")
        sign.click_continue()
        sign.enter_firstname("Swati")
        sign.enter_lastname("Gogia")
        sign.enter_mobile_no("9956400901")
        sign.enter_organisation_name("Inventum")
        sign.enter_city("Noida")
        sign.enter_state("UP")
        sign.enter_country("India")
        sign.enter_pincode("201301")
        sign.enter_shipping_add(streetName)
        sign.enter_billing_add(streetName)
        sign.enter_gst("GSTIN02248601")
        sign.click_continue()
        iframe = driver.find_element(By.XPATH, '//iframe[@class="razorpay-checkout-frame"]')
        driver.switch_to.frame(iframe)
        sign.click_upi_qr()
        time.sleep(1)
        sign.click_upi_id()
        time.sleep(2)
        sign.enter_upi_id("test@icici")
        time.sleep(2)
        webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
        driver.switch_to.default_content()


        time.sleep(5)



    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/home/priyansu/Desktop/testing/unifyng-automation-testing/UnifyNG/Reports"))