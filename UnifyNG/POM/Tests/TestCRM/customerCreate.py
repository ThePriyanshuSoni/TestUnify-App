from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
from UnifyNG.POM.Pages.Login.loginPage import LoginPage
from UnifyNG.POM.Pages.Dashboard.dashboardPage import DashboardPage
from UnifyNG.POM.Pages.CRM.customerListingPage import CustomerListingPage
from UnifyNG.POM.Pages.CRM.addCustomerPage import AddCustomerPage



class TestCustomerCreate(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01_valid_create(self):
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
        dashboard.click_crm()
        dashboard.click_customers()
        time.sleep(2)
        dashboard.click_add_new()

        # listing = CustomerListingPage()
        # listing.click_add_new()

        customer = AddCustomerPage(driver)
        customer.enter_customerid("IND003472")
        customer.enter_firstname("Priyanshu1")
        customer.enter_lastname("Soni1")
        customer.click_biller()
        customer.select_biller()
        customer.click_label()
        customer.select_label(Keys.ARROW_DOWN, Keys.ENTER)
        customer.enter_notes("Hello There this is UnifyNG, How May i help you :)")
        customer.enter_email("testing@gmail.com")
        customer.enter_mobile("9191919191")
        customer.enter_name("Priyanshu Test")
        customer.enter_address_line("TG1 Xerex, MG Road, Santa Cruz, Vasi")
        customer.enter_landmark("Near Walmart Store")
        customer.enter_pincode("100211")
        customer.enter_city("Mumbai")
        customer.click_country()
        customer.select_country()
        customer.click_state()
        time.sleep(3)
        customer.select_state()
        customer.enter_comment("Testing")
        time.sleep(2)
        customer.click_save()
        time.sleep(5)










    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Pass")

