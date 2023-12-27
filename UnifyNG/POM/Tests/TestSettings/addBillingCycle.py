import HtmlTestRunner
from faker import Faker
from selenium import webdriver
import time
import unittest

from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from UnifyNG.POM.Pages.Login.loginPage import LoginPage
from UnifyNG.POM.Pages.Dashboard.dashboardPage import DashboardPage
from UnifyNG.POM.Pages.Settings.SiteSettings.BillingCycle.addBillingCyclePage import AddBillingCyclePage

fake = Faker(['en_US'])
fake_word = fake.word()
fake_name = fake.user_name()
cycleName = fake.street_name()
num = fake.random_int(min=1, max=100)


class TestAddBillingCycle(unittest.TestCase):
    base_dev_url = "https://unifyng.inventum.co/login"
    priyanshu_tenant = "https://priyanshu.inventum.co/"

    @classmethod
    def setUp(cls):
        chrome_options = Options()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--disable-gpu')
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    # def test_001_billCycle(self):
    #     driver = self.driver
    #     driver.get(self.base_dev_url)
    #
    #     login = LoginPage(driver)
    #     login.enter_tenant("priyanshu")
    #     login.enter_continue()
    #     login.enter_username("priyanshu")
    #     login.enter_password("password")
    #     login.click_login()
    #     time.sleep(2)
    #
    #     dashboard = DashboardPage(driver)
    #     dashboard.click_settings()
    #     dashboard.click_site_settings()
    #     dashboard.click_billing_cycle()
    #     time.sleep(5)
    #     cycle = AddBillingCyclePage(driver)
    #     cycle.click_add_billing_cycle()
    #     time.sleep(1)
    #     cycle.enter_billing_cycle_name(cycleName)
    #     cycle.click_billing_frequency()
    #     time.sleep(1)
    #     webdriver.ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()
    #     time.sleep(1)
    #     webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
    #     time.sleep(1)
    #     cycle.click_billing_date()
    #     time.sleep(1)
    #     webdriver.ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()
    #     time.sleep(1)
    #     webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
    #     time.sleep(1)
    #     cycle.click_enable_toggle_button()
    #     cycle.click_save()
    #     time.sleep(1)
    #     text = driver.find_element(By.XPATH, "//div[@role='alert']").text
    #     popup = "Billing Cycle Saved Successfully"
    #     if text in popup:
    #         print(f"Valid Alert:> {popup}.")
    #     else:
    #         print(f"Invalid Alert:> {text}.")
    #     time.sleep(1)
    #     dashboard.click_account()
    #     time.sleep(1)
    #     dashboard.click_logout()
    #
    #
    # def test_002_billCycle(self):
    #     driver = self.driver
    #     driver.get(self.base_dev_url)
    #
    #     login = LoginPage(driver)
    #     login.enter_tenant("priyanshu")
    #     login.enter_continue()
    #     login.enter_username("priyanshu")
    #     login.enter_password("password")
    #     login.click_login()
    #     time.sleep(2)
    #
    #     dashboard = DashboardPage(driver)
    #     dashboard.click_settings()
    #     dashboard.click_site_settings()
    #     dashboard.click_billing_cycle()
    #     time.sleep(5)
    #     cycle = AddBillingCyclePage(driver)
    #     cycle.click_action_three_dot()
    #     time.sleep(1)
    #     cycle.click_action_edit()
    #     time.sleep(1)
    #     cycle.enter_billing_cycle_name("a")
    #     cycle.click_save()
    #     time.sleep(1)
    #     text = driver.find_element(By.XPATH, "//div[@role='alert']").text
    #     popup = "Bill Cycle updated successfully"
    #     if text in popup:
    #         print(f"Valid Alert:> {popup}.")
    #     else:
    #         print(f"Invalid Alert:> {text}.")
    #     time.sleep(1)
    #     dashboard.click_account()
    #     time.sleep(1)
    #     dashboard.click_logout()
    #
    #
    # def test_003_billCycle(self):
    #     driver = self.driver
    #     driver.get(self.base_dev_url)
    #
    #     login = LoginPage(driver)
    #     login.enter_tenant("priyanshu")
    #     login.enter_continue()
    #     login.enter_username("priyanshu")
    #     login.enter_password("password")
    #     login.click_login()
    #     time.sleep(2)
    #
    #     dashboard = DashboardPage(driver)
    #     dashboard.click_settings()
    #     dashboard.click_site_settings()
    #     dashboard.click_billing_cycle()
    #     time.sleep(2)
    #     cycle = AddBillingCyclePage(driver)
    #     cycle.click_add_billing_cycle()
    #     time.sleep(1)
    #     cycle.click_save()
    #     time.sleep(1)
    #
    #     billingCycle = driver.find_element(By.ID, "billingCycleName-helper-text").text
    #     popup1 = "Billing Cycle Name cannot be blank!"
    #     if billingCycle in popup1:
    #         print(f"Valid Alert:> {popup1}.")
    #     else:
    #         print(f"Invalid Alert:> {billingCycle}.")
    #
    #     billingFrequency = driver.find_element(By.XPATH, "//p[normalize-space()='Billing Frequency cannot be empty']").text
    #     popup2 = "Billing Frequency cannot be empty"
    #     if billingFrequency in popup2:
    #         print(f"Valid Alert:> {popup2}.")
    #     else:
    #         print(f"Invalid Alert:> {billingFrequency}.")
    #
    #     billingDate = driver.find_element(By.XPATH, "//p[normalize-space()='Date Of Billing cannot be empty']").text
    #     popup3 = "Date Of Billing cannot be empty"
    #     if billingDate in popup3:
    #         print(f"Valid Alert:> {popup3}.")
    #     else:
    #         print(f"Invalid Alert:> {billingDate}.")
    #
    #     webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    #     time.sleep(1)
    #     dashboard.click_account()
    #     time.sleep(1)
    #     dashboard.click_logout()


    # def test_004_billCycle(self):
    #     driver = self.driver
    #     driver.get(self.base_dev_url)
    #
    #     login = LoginPage(driver)
    #     login.enter_tenant("priyanshu")
    #     login.enter_continue()
    #     login.enter_username("priyanshu")
    #     login.enter_password("password")
    #     login.click_login()
    #     time.sleep(2)
    #
    #     dashboard = DashboardPage(driver)
    #     dashboard.click_settings()
    #     dashboard.click_site_settings()
    #     dashboard.click_billing_cycle()
    #     time.sleep(2)
    #     cycle = AddBillingCyclePage(driver)
    #     cycle.click_add_billing_cycle()
    #     time.sleep(1)
    #     cycle.enter_billing_cycle_name("+@__-")
    #     time.sleep(1)
    #     cycle.click_enable_toggle_button()
    #     cycle.click_save()
    #     time.sleep(1)
    #
    #     billingCycle = driver.find_element(By.ID, "billingCycleName-helper-text").text
    #     popup1 = "Billing Cycle cannot be empty"
    #     if billingCycle in popup1:
    #         print(f"Valid Alert:> {popup1}.")
    #     else:
    #         print(f"Invalid Alert:> {billingCycle}.")
    #
    #     billingFrequency = driver.find_element(By.XPATH, "//p[normalize-space()='Billing Frequency cannot be empty']").text
    #     popup2 = "Billing Frequency cannot be empty"
    #     if billingFrequency in popup2:
    #         print(f"Valid Alert:> {popup2}.")
    #     else:
    #         print(f"Invalid Alert:> {billingFrequency}.")
    #
    #     billingDate = driver.find_element(By.XPATH, "//p[normalize-space()='Date Of Billing cannot be empty']").text
    #     popup3 = "Date Of Billing cannot be empty"
    #     if billingDate in popup3:
    #         print(f"Valid Alert:> {popup3}.")
    #     else:
    #         print(f"Invalid Alert:> {billingDate}.")
    #     webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    #     time.sleep(1)
    #     dashboard.click_account()
    #     time.sleep(1)
    #     dashboard.click_logout()


    # def test_005_billCycle(self):
    #     driver = self.driver
    #     driver.get(self.base_dev_url)
    #
    #     login = LoginPage(driver)
    #     login.enter_tenant("priyanshu")
    #     login.enter_continue()
    #     login.enter_username("priyanshu")
    #     login.enter_password("password")
    #     login.click_login()
    #     time.sleep(2)
    #
    #     dashboard = DashboardPage(driver)
    #     dashboard.click_settings()
    #     dashboard.click_site_settings()
    #     dashboard.click_billing_cycle()
    #     time.sleep(2)
    #     text1 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/main[1]/div[3]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]").text
    #     cycle = AddBillingCyclePage(driver)
    #     cycle.click_add_billing_cycle()
    #     time.sleep(1)
    #     cycle.enter_billing_cycle_name(text1)
    #     cycle.click_billing_frequency()
    #     time.sleep(1)
    #     webdriver.ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()
    #     time.sleep(1)
    #     webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
    #     time.sleep(1)
    #     cycle.click_billing_date()
    #     time.sleep(1)
    #     webdriver.ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()
    #     time.sleep(1)
    #     webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
    #     time.sleep(1)
    #     cycle.click_enable_toggle_button()
    #     cycle.click_save()
    #     time.sleep(1)
    #
    #     text2 = driver.find_element(By.XPATH, "//div[@role='alert']").text
    #     popup = "date or day already exist"
    #     if text2 in popup:
    #         print(f"Valid Alert:> {popup}.")
    #     else:
    #         print(f"Invalid Alert:> {text2}.")
    #     webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    #     time.sleep(1)
    #     dashboard.click_account()
    #     time.sleep(1)
    #     dashboard.click_logout()


    def test_006_billCycle(self):
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
        dashboard.click_billing_cycle()
        time.sleep(5)
        cycle = AddBillingCyclePage(driver)
        cycle.click_add_billing_cycle()
        time.sleep(1)
        cycle.enter_billing_cycle_name(cycleName)
        cycle.click_billing_frequency()
        time.sleep(1)
        webdriver.ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()
        time.sleep(1)
        webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
        time.sleep(1)
        cycle.click_billing_date()
        time.sleep(1)
        webdriver.ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()
        time.sleep(1)
        webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
        time.sleep(1)
        cycle.click_enable_toggle_button()
        cycle.click_save()
        time.sleep(1)
        text = driver.find_element(By.XPATH, "//div[@role='alert']").text
        popup = "date or day already exist"
        if text in popup:
            print(f"Valid Alert:> {popup}.")
        else:
            print(f"Invalid Alert:> {text}.")
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

