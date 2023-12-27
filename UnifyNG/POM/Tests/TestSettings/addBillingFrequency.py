import HtmlTestRunner
from faker import Faker
from selenium import webdriver
import time
import unittest

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from UnifyNG.POM.Pages.Login.loginPage import LoginPage
from UnifyNG.POM.Pages.Dashboard.dashboardPage import DashboardPage
from UnifyNG.POM.Pages.Settings.SiteSettings.BillingFrequency.addBillingFrequencyPage import AddBillingFrequencyPage


fake = Faker(['en_US'])
fake_word = fake.word()
fake_name = fake.user_name()
num = fake.random_int(min=1, max=100)



class TestAddBillingFrequency(unittest.TestCase):
    base_dev_url = "https://unifyng.inventum.co/login"
    priyanshu_tenant = "http://priyanshu.inventum.co/"

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    def test_001_billFreq(self):
        driver = self.driver
        driver.get(self.base_dev_url)

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
        dashboard.click_billing_frequency()

        freq = AddBillingFrequencyPage(driver)
        freq.click_add_new()
        time.sleep(1)
        freq.enter_frequency_name(fake_name)
        time.sleep(1)
        freq.click_billing_frequency()
        freq.select_week()
        time.sleep(1)
        freq.enter_count(num)
        time.sleep(1)
        freq.click_save()
        time.sleep(2)
        text = driver.find_element(By.XPATH, "//div[@role='alert']").text
        popup = "Billing Frequency data saved Successfully"
        if text in popup:
            print(f"Valid Alert:> {popup}.")
        else:
            print(f"Invalid Alert:> {text}.")

        time.sleep(1)
        dashboard.click_account()
        time.sleep(1)
        dashboard.click_logout()


    def test_002_billFreq(self):
        driver = self.driver
        driver.get(self.base_dev_url)

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
        dashboard.click_billing_frequency()

        freq = AddBillingFrequencyPage(driver)
        freq.click_add_new()
        time.sleep(1)
        freq.click_save()
        time.sleep(1)

        frequencyName = driver.find_element(By.ID, "billingFrequencyName-helper-text").text
        popup1 = "Billing Frequency Name cannot be blank!"
        if frequencyName in popup1:
            print(f"Valid Alert:> {popup1}.")
        else:
            print(f"Invalid Alert:> {frequencyName}.")

        billingFrequency = driver.find_element(By.XPATH, "//p[@class='MuiFormHelperText-root MuiFormHelperText-sizeSmall MuiFormHelperText-contained error css-1l18pnj-MuiFormHelperText-root']").text
        popup2 = "Please select billing frequency!"
        if billingFrequency in popup2:
            print(f"Valid Alert:> {popup2}.")
        else:
            print(f"Invalid Alert:> {billingFrequency}.")

        frequencyCount = driver.find_element(By.ID, "billingFrequencyCount-helper-text").text
        popup3 = "Billing Frequency Count cannot be blank!"
        if frequencyCount in popup3:
            print(f"Valid Alert:> {popup3}.")
        else:
            print(f"Invalid Alert:> {frequencyCount}.")

        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        time.sleep(1)
        dashboard.click_account()
        time.sleep(1)
        dashboard.click_logout()


    def test_003_billFreq(self):
        driver = self.driver
        driver.get(self.base_dev_url)

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
        dashboard.click_billing_frequency()

        freq = AddBillingFrequencyPage(driver)
        freq.click_add_new()
        time.sleep(1)
        freq.enter_frequency_name("Hello There")
        time.sleep(1)
        freq.enter_count("101")
        freq.click_save()
        time.sleep(1)

        frequencyName = driver.find_element(By.ID, "billingFrequencyName-helper-text").text
        popup1 = " Only alphabets are allowed with no space before and after!"
        if frequencyName in popup1:
            print(f"Valid Alert:> {popup1}.")
        else:
            print(f"Invalid Alert:> {frequencyName}.")

        frequencyCount = driver.find_element(By.ID, "billingFrequencyCount-helper-text").text
        popup2 = "Please enter valid count range 1-100!"
        if frequencyCount in popup2:
            print(f"Valid Alert:> {popup2}.")
        else:
            print(f"Invalid Alert:> {frequencyCount}.")

        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        time.sleep(1)
        dashboard.click_account()
        time.sleep(1)
        dashboard.click_logout()


    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()



if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/home/priyansu/Desktop/testing/unifyng-automation-testing/UnifyNG/Reports"))


