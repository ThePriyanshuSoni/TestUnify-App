from selenium import webdriver
import HtmlTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import time
import unittest
import string
from UnifyNG.POM.Pages.Login.loginPage import LoginPage
from UnifyNG.POM.Pages.Dashboard.dashboardPage import DashboardPage
from UnifyNG.POM.Pages.CRM.addCustomerPage import AddCustomerPage



class TestCustomerCreate(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    # def test_001_crm(self):
    #     driver = self.driver
    #     driver.get("http://unifyng.inventum.co/login")
    #
    #     login = LoginPage(driver)
    #     login.enter_tenant("priyanshu")
    #     login.enter_continue()
    #     login.enter_username("priyanshu")
    #     login.enter_password("password")
    #     login.click_login()
    #
    #     dashboard = DashboardPage(driver)
    #     time.sleep(3)
    #     dashboard.click_crm()
    #     dashboard.click_customers()
    #     time.sleep(2)
    #     dashboard.click_add_new()
    #
    #     customer = AddCustomerPage(driver)
    #     customer.enter_customerid()
    #     customer.enter_firstname()
    #     customer.click_biller()
    #     customer.select_biller(Keys.ARROW_DOWN, Keys.ENTER)
    #     customer.enter_email("testing@gmail.com")
    #     customer.enter_mobile()
    #     customer.enter_name("Priyanshu Test")
    #     customer.enter_address_line("TG1 Xerex, MG Road, Santa Cruz, Vasi")
    #     customer.click_country()
    #     customer.select_country()
    #     customer.click_state()
    #     time.sleep(3)
    #     customer.select_state()
    #     customer.enter_city("Mumbai")
    #     customer.enter_pincode("100211")
    #     dashboard.page_scroll_to_top()
    #     time.sleep(2)
    #     customer.click_save()
    #     time.sleep(3)
    #     dashboard.click_account()
    #     time.sleep(2)
    #     dashboard.click_logout()
    #     time.sleep(2)
    #

    # def test_002_crm(self):
    #     driver = self.driver
    #     driver.get("http://unifyng.inventum.co/login")
    #
    #     login = LoginPage(driver)
    #     login.enter_tenant("priyanshu")
    #     login.enter_continue()
    #     login.enter_username("priyanshu")
    #     login.enter_password("password")
    #     login.click_login()
    #
    #     dashboard = DashboardPage(driver)
    #     time.sleep(3)
    #     dashboard.click_crm()
    #     dashboard.click_customers()
    #     time.sleep(2)
    #     dashboard.click_add_new()
    #
    #     # listing = CustomerListingPage()
    #     # listing.click_add_new()
    #
    #     customer = AddCustomerPage(driver)
    #     customer.enter_customerid()
    #     customer.enter_firstname()
    #     customer.enter_lastname()
    #     customer.click_biller()
    #     customer.select_biller(Keys.ARROW_DOWN, Keys.ENTER)
    #     customer.click_label()
    #     customer.select_label(Keys.ARROW_UP, Keys.ENTER)
    #     customer.enter_notes("Hello There this is UnifyNG, How May i help you :)")
    #     customer.enter_email("testing@gmail.com")
    #     customer.enter_mobile()
    #     customer.enter_name("Priyanshu Test")
    #     customer.enter_address_line("TG1 Xerex, MG Road, Santa Cruz, Vasi")
    #     customer.enter_landmark("Near Walmart Store")
    #     customer.enter_pincode("100211")
    #     customer.enter_city("Mumbai")
    #     customer.click_country()
    #     customer.select_country()
    #     customer.click_state()
    #     time.sleep(3)
    #     customer.select_state()
    #     customer.enter_comment("Testing")
    #     dashboard.page_scroll_to_top()
    #     time.sleep(2)
    #     customer.click_save()
    #     time.sleep(3)
    #     dashboard.click_account()
    #     time.sleep(2)
    #     dashboard.click_logout()
    #     time.sleep(5)
    #
    #
    def test_003_crm(self):
        driver = self.driver
        driver.get("http://unifyng.inventum.co/login")

        login = LoginPage(driver)
        login.enter_tenant("priyanshu")
        login.enter_continue()
        login.enter_username("priyanshu")
        login.enter_password("password")
        login.click_login()

        dashboard = DashboardPage(driver)
        time.sleep(3)
        dashboard.click_crm()
        dashboard.click_customers()
        time.sleep(2)
        dashboard.click_add_new()

        customer = AddCustomerPage(driver)
        customer.click_save()
        time.sleep(3)
        error = driver.find_element(By.XPATH, "//div[contains(text(),'Please check the form carefully for errors!')]").text
        popup_text = "Please check the form carefully for errors!"
        if popup_text in error:
            print(f"Valid Error:> {popup_text}.")
        else:
            print(f"Invalid Error:> {error}.")

        time.sleep(3)
        dashboard.click_account()
        time.sleep(2)
        dashboard.click_logout()
        time.sleep(2)
    #
    #
    # def test_004_crm(self):
    #     driver = self.driver
    #     driver.get("http://unifyng.inventum.co/login")
    #
    #     login = LoginPage(driver)
    #     login.enter_tenant("priyanshu")
    #     login.enter_continue()
    #     login.enter_username("priyanshu")
    #     login.enter_password("password")
    #     login.click_login()
    #
    #     dashboard = DashboardPage(driver)
    #     time.sleep(3)
    #     dashboard.click_crm()
    #     dashboard.click_customers()
    #     time.sleep(2)
    #     dashboard.click_add_new()
    #
    #     customer = AddCustomerPage(driver)
    #     customer.click_auto_generate()
    #     customer.enter_firstname()
    #     customer.click_biller()
    #     customer.select_biller(Keys.ARROW_DOWN, Keys.ENTER)
    #     customer.enter_email("testing@gmail.com")
    #     customer.enter_mobile()
    #     customer.enter_name("Priyanshu Test")
    #     customer.enter_address_line("TG1 Xerex, MG Road, Santa Cruz, Vasi")
    #     customer.click_country()
    #     customer.select_country()
    #     customer.click_state()
    #     time.sleep(3)
    #     customer.select_state()
    #     customer.enter_city("Mumbai")
    #     customer.enter_pincode("100211")
    #     dashboard.page_scroll_to_top()
    #     time.sleep(2)
    #     customer.click_save()
    #     time.sleep(3)
    #     dashboard.click_account()
    #     time.sleep(2)
    #     dashboard.click_logout()
    #     time.sleep(2)

    def test_005_crm(self):
        driver = self.driver
        driver.get("http://unifyng.inventum.co/login")

        login = LoginPage(driver)
        login.enter_tenant("priyanshu")
        login.enter_continue()
        login.enter_username("priyanshu")
        login.enter_password("password")
        login.click_login()

        dashboard = DashboardPage(driver)
        time.sleep(3)
        dashboard.click_crm()
        dashboard.click_customers()
        time.sleep(2)
        dashboard.click_add_new()

        customer = AddCustomerPage(driver)
        customer.click_auto_generate()
        customer.enter_firstname()
        customer.click_biller()
        customer.select_biller(Keys.ARROW_DOWN, Keys.ENTER)
        customer.enter_email("testing@gmail.com")
        customer.enter_mobile()
        customer.enter_name("Priyanshu Test")
        customer.enter_address_line("TG1 Xerex, MG Road, Santa Cruz, Vasi")
        customer.click_country()
        customer.select_country()
        customer.click_state()
        time.sleep(3)
        customer.select_state()
        customer.enter_city("Mumbai")
        customer.enter_pincode("100211")
        dashboard.page_scroll_to_top()
        time.sleep(2)
        customer.click_save()
        time.sleep(3)
        error = driver.find_element(By.XPATH, "//div[@role='alert']").text
        popup_text = "Recipe for customer module is not created"
        if popup_text in error:
            print(f"Valid Error (When recipe is not created):> {popup_text}.")
        else:
            print(f"Invalid Error (When recipe is setup):> {error}.")
        time.sleep(3)
        dashboard.click_account()
        time.sleep(2)
        dashboard.click_logout()
        time.sleep(2)





    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()


n = 7
m = 10
name = ''.join(random.choices(string.ascii_lowercase, k=8))
randomName = str(name)

randomMobile = ''.join(random.choices(string.octdigits, k=m))
randomStrUpper = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/home/priyansu/Desktop/testing/unifyng-automation-testing/UnifyNG/Reports"))


