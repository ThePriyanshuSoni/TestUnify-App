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
from selenium.webdriver.common.alert import Alert


class TestCustomerCreate(unittest.TestCase):

    base_dev_url = "https://unifyng.inventum.co/login"
    priyanshu_tenant = "http://priyanshu.inventum.co/"


    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_001_crm(self):
        driver = self.driver
        driver.get(self.base_dev_url)

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
        customer.enter_customerid()
        customer.enter_firstname(''.join(random.choices(string.ascii_lowercase, k=8)))
        customer.click_biller()
        customer.select_biller(Keys.ARROW_DOWN, Keys.ENTER)
        customer.enter_email("testing@gmail.com")
        customer.enter_mobile(''.join(random.choices(string.octdigits, k=10)))
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
        dashboard.click_account()
        time.sleep(2)
        dashboard.click_logout()
        time.sleep(2)


    def test_002_crm(self):
        driver = self.driver
        driver.get(self.base_dev_url)

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
        customer.enter_customerid()
        customer.enter_firstname(''.join(random.choices(string.ascii_lowercase, k=8)))
        customer.enter_lastname()
        customer.click_biller()
        customer.select_biller(Keys.ARROW_DOWN, Keys.ENTER)
        customer.click_label()
        customer.select_label(Keys.ARROW_UP, Keys.ENTER)
        customer.enter_notes("Hello There this is UnifyNG, How May i help you :)")
        customer.enter_email("testing@gmail.com")
        customer.enter_mobile(''.join(random.choices(string.octdigits, k=10)))
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
        dashboard.page_scroll_to_top()
        time.sleep(2)
        customer.click_save()
        time.sleep(3)
        dashboard.click_account()
        time.sleep(2)
        dashboard.click_logout()
        time.sleep(5)


    def test_003_crm(self):
        driver = self.driver
        driver.get(self.base_dev_url)

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


    def test_004_crm(self):
        driver = self.driver
        driver.get(self.base_dev_url)

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
        customer.enter_firstname(''.join(random.choices(string.ascii_lowercase, k=8)))
        customer.click_biller()
        customer.select_biller(Keys.ARROW_DOWN, Keys.ENTER)
        customer.enter_email("testing@gmail.com")
        customer.enter_mobile(''.join(random.choices(string.octdigits, k=10)))
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
        dashboard.click_account()
        time.sleep(2)
        dashboard.click_logout()
        time.sleep(2)

    def test_005_crm(self):
        driver = self.driver
        driver.get(self.base_dev_url)

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
        customer.enter_firstname(''.join(random.choices(string.ascii_lowercase, k=8)))
        customer.click_biller()
        customer.select_biller(Keys.ARROW_DOWN, Keys.ENTER)
        customer.enter_email("testing@gmail.com")
        customer.enter_mobile(''.join(random.choices(string.octdigits, k=10)))
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

    def test_006_crm(self):
        driver = self.driver
        driver.get(self.base_dev_url)

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
        customer.enter_firstname("[]@#")
        customer.click_save()
        time.sleep(1)
        error = driver.find_element(By.XPATH, "//p[@id='firstName-helper-text']").text
        popup_text = "Please enter First Name!"
        if error in popup_text:
            print(f"Valid Error:> {popup_text}.")
        else:
            print(f"Invalid Error:> {error}.")
        time.sleep(1)
        dashboard.click_account()
        time.sleep(2)
        dashboard.click_logout()
        time.sleep(2)

    def test_007_crm(self):
        driver = self.driver
        driver.get(self.base_dev_url)

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
        customer.enter_email("abc")
        dashboard.page_scroll_to_top()
        customer.click_save()
        time.sleep(1)
        error = driver.find_element(By.XPATH, "//p[@id='email-helper-text']").text
        popup_text = "Please enter valid Email!"
        if error in popup_text:
            print(f"Valid Error:> {popup_text}.")
        else:
            print(f"Invalid Error:> {error}.")
        time.sleep(1)
        dashboard.click_account()
        time.sleep(2)
        dashboard.click_logout()
        time.sleep(2)

    def test_008_crm(self):
        driver = self.driver
        driver.get(self.base_dev_url)

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
        customer.enter_mobile("abc")
        dashboard.page_scroll_to_top()
        customer.click_save()
        time.sleep(1)
        error = driver.find_element(By.XPATH, "//p[@id='phoneNo-helper-text']").text
        popup_text = "Contact Number cannot be blank!"
        if error in popup_text:
            print(f"Valid Error:> {popup_text}.")
        else:
            print(f"Invalid Error:> {error}.")
        time.sleep(1)
        dashboard.click_account()
        time.sleep(2)
        dashboard.click_logout()
        time.sleep(2)

    def test_009_crm(self):
        driver = self.driver
        driver.get(self.base_dev_url)

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
        customer.enter_name("@=[]")
        customer.enter_city("12345")
        customer.enter_pincode("abcde")
        dashboard.page_scroll_to_top()
        customer.click_save()
        time.sleep(1)
        namemsg = driver.find_element(By.XPATH, "//p[@id='firstName-helper-text']").text
        citymsg = driver.find_element(By.XPATH, "//p[@id='city-helper-text']").text
        pincodemsg = driver.find_element(By.XPATH, "//p[@id='pincode-helper-text']").text
        print(namemsg)
        print(citymsg)
        print(pincodemsg)

        time.sleep(1)
        dashboard.click_account()
        time.sleep(2)
        dashboard.click_logout()
        time.sleep(2)

    def test_010_crm(self):
        driver = self.driver
        driver.get(self.base_dev_url)

        login = LoginPage(driver)
        login.enter_tenant("priyanshu")
        login.enter_continue()
        login.enter_username("priyanshu")
        login.enter_password("password")
        login.click_login()

        dashboard = DashboardPage(driver)
        customer = AddCustomerPage(driver)
        time.sleep(3)
        dashboard.click_crm()
        dashboard.click_customers()
        time.sleep(2)
        customer.click_action_three_dot()
        customer.click_action_edit()
        customer.enter_firstname(Keys.CONTROL + "a")
        customer.enter_firstname(Keys.BACKSPACE)
        customer.enter_firstname("updated name testing")
        time.sleep(1)
        dashboard.page_scroll_to_top()
        customer.click_save()
        time.sleep(1)
        error = driver.find_element(By.XPATH, "//div[@role='alert']").text
        popup_text = "Customer Updated successfully!"
        if error in popup_text:
            print(f"Valid Error:> {popup_text}.")
        else:
            print(f"Invalid Error:> {error}.")
        time.sleep(1)
        dashboard.click_account()
        time.sleep(2)
        dashboard.click_logout()
        time.sleep(2)

    def test_011_crm(self):
        driver = self.driver
        driver.get(self.base_dev_url)

        login = LoginPage(driver)
        login.enter_tenant("priyanshu")
        login.enter_continue()
        login.enter_username("priyanshu")
        login.enter_password("password")
        login.click_login()

        dashboard = DashboardPage(driver)
        customer = AddCustomerPage(driver)
        time.sleep(3)
        dashboard.click_crm()
        dashboard.click_customers()
        time.sleep(2)
        customer.click_action_three_dot()
        customer.click_action_edit()
        customer.click_address_book()
        time.sleep(1)
        customer.click_edit_address_details()
        customer.enter_name(Keys.CONTROL + "a")
        customer.enter_name(Keys.BACKSPACE)
        customer.enter_name("Priyanshu")
        time.sleep(5)
        dashboard.page_scroll_to_top()
        customer.click_save()
        time.sleep(1)
        error = driver.find_element(By.XPATH, "//div[@role='alert']").text
        popup_text = "Customer address updated successfully!"
        if error in popup_text:
            print(f"Valid Error:> {popup_text}.")
        else:
            print(f"Invalid Error:> {error}.")
        time.sleep(1)
        dashboard.click_account()
        time.sleep(2)
        dashboard.click_logout()
        time.sleep(2)

    def test_012_crm(self):
        driver = self.driver
        driver.get(self.base_dev_url)

        login = LoginPage(driver)
        login.enter_tenant("priyanshu")
        login.enter_continue()
        login.enter_username("priyanshu")
        login.enter_password("password")
        login.click_login()

        dashboard = DashboardPage(driver)
        customer = AddCustomerPage(driver)
        time.sleep(3)
        dashboard.click_crm()
        dashboard.click_customers()
        time.sleep(2)
        customer.click_action_three_dot()
        customer.click_action_delete()
        time.sleep(2)
        alert = Alert(driver)
        alert.accept()
        time.sleep(2)
        error = driver.find_element(By.XPATH, "//div[@role='alert']").text
        popup_text = "Customer Deleted successfully"
        if error in popup_text:
            print(f"Valid Error:> {popup_text}.")
        else:
            print(f"Invalid Error:> {error}.")

        time.sleep(1)
        dashboard.click_account()
        time.sleep(2)
        dashboard.click_logout()
        time.sleep(2)

    def test_013_crm(self):
        driver = self.driver
        driver.get(self.base_dev_url)

        login = LoginPage(driver)
        login.enter_tenant("priyanshu")
        login.enter_continue()
        login.enter_username("priyanshu")
        login.enter_password("password")
        login.click_login()

        dashboard = DashboardPage(driver)
        customer = AddCustomerPage(driver)
        time.sleep(3)
        dashboard.click_crm()
        dashboard.click_customers()
        time.sleep(1)
        customer.click_table_view()
        customer.click_preview_mode()
        time.sleep(2)
        customer.click_first_customer_on_table()
        time.sleep(1)
        customer.click_second_customer_on_table()
        time.sleep(1)
        customer.click_table_view()
        customer.click_default()
        time.sleep(1)
        dashboard.click_account()
        time.sleep(2)
        dashboard.click_logout()
        time.sleep(2)

    def test_014_crm(self):
        driver = self.driver
        driver.get(self.base_dev_url)

        login = LoginPage(driver)
        login.enter_tenant("priyanshu")
        login.enter_continue()
        login.enter_username("priyanshu")
        login.enter_password("password")
        login.click_login()

        dashboard = DashboardPage(driver)
        customer = AddCustomerPage(driver)
        time.sleep(3)
        dashboard.click_crm()
        dashboard.click_customers()
        time.sleep(1)
        text1 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/main[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]").text
        customer.enter_search_filter(text1)
        customer.enter_search_filter(Keys.ENTER)
        time.sleep(1)
        text2 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/main[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]").text

        if text2 in text1:
            print(f"Valid Customer ID:> {text1}.")
        else:
            print(f"Invalid Customer ID:> {text2}.")

        time.sleep(1)
        dashboard.click_account()
        time.sleep(2)
        dashboard.click_logout()
        time.sleep(2)

    def test_015_crm(self):
        driver = self.driver
        driver.get(self.base_dev_url)

        login = LoginPage(driver)
        login.enter_tenant("priyanshu")
        login.enter_continue()
        login.enter_username("priyanshu")
        login.enter_password("password")
        login.click_login()

        dashboard = DashboardPage(driver)
        customer = AddCustomerPage(driver)
        time.sleep(3)
        dashboard.click_crm()
        dashboard.click_customers()
        time.sleep(1)
        text1 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/main[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]").text
        customer.enter_search_filter(text1)
        customer.enter_search_filter(Keys.ENTER)
        time.sleep(1)
        customer.click_filter_icon()
        customer.click_search_by_email()
        time.sleep(1)
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        text2 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/main[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]").text

        if text2 in text1:
            print(f"Valid Customer Email:> {text1}.")
        else:
            print(f"Invalid Customer Email:> {text2}.")
        time.sleep(1)
        dashboard.click_account()
        time.sleep(2)
        dashboard.click_logout()
        time.sleep(2)

    def test_016_crm(self):
        driver = self.driver
        driver.get(self.base_dev_url)

        login = LoginPage(driver)
        login.enter_tenant("priyanshu")
        login.enter_continue()
        login.enter_username("priyanshu")
        login.enter_password("password")
        login.click_login()

        dashboard = DashboardPage(driver)
        customer = AddCustomerPage(driver)
        time.sleep(3)
        dashboard.click_crm()
        dashboard.click_customers()
        time.sleep(1)
        text1 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/main[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]").text
        customer.enter_search_filter(text1)
        customer.enter_search_filter(Keys.ENTER)
        time.sleep(1)
        customer.click_filter_icon()
        customer.click_search_by_contact_no()
        time.sleep(1)
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        text2 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/main[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]").text

        if text2 in text1:
            print(f"Valid Customer Contact No:> {text1}.")
        else:
            print(f"Invalid Customer Contact No:> {text2}.")
        time.sleep(1)
        dashboard.click_account()
        time.sleep(2)
        dashboard.click_logout()
        time.sleep(2)

    def test_017_crm(self):
        driver = self.driver
        driver.get(self.base_dev_url)

        login = LoginPage(driver)
        login.enter_tenant("priyanshu")
        login.enter_continue()
        login.enter_username("priyanshu")
        login.enter_password("password")
        login.click_login()

        dashboard = DashboardPage(driver)
        customer = AddCustomerPage(driver)
        time.sleep(3)
        dashboard.click_crm()
        dashboard.click_customers()
        time.sleep(1)
        text1 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/main[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]").text
        customer.enter_search_filter(text1)
        customer.enter_search_filter(Keys.ENTER)
        time.sleep(1)
        customer.click_filter_icon()
        customer.click_search_by_name()
        time.sleep(1)
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        text2 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/main[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]").text

        if text2 in text1:
            print(f"Valid Customer Name:> {text1}.")
        else:
            print(f"Invalid Customer Name:> {text2}.")
        time.sleep(1)
        dashboard.click_account()
        time.sleep(2)
        dashboard.click_logout()
        time.sleep(2)

    def test_018_crm(self):
        driver = self.driver
        driver.get(self.base_dev_url)

        login = LoginPage(driver)
        login.enter_tenant("priyanshu")
        login.enter_continue()
        login.enter_username("priyanshu")
        login.enter_password("password")
        login.click_login()

        dashboard = DashboardPage(driver)
        customer = AddCustomerPage(driver)
        time.sleep(3)
        dashboard.click_crm()
        dashboard.click_customers()
        time.sleep(1)
        text1 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/main[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]").text
        customer.enter_search_filter(text1)
        customer.enter_search_filter(Keys.ENTER)
        time.sleep(1)
        customer.click_filter_icon()
        customer.click_search_by_email()
        customer.click_search_by_contact_no()
        customer.click_search_by_name()
        time.sleep(1)
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        text2 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/main[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]").text

        if text2 in text1:
            print(f"Valid Customer Name:> {text1}.")
        else:
            print(f"Invalid Customer Name:> {text2}.")
        time.sleep(1)
        dashboard.click_account()
        time.sleep(2)
        dashboard.click_logout()
        time.sleep(2)

    def test_019_crm(self):
        driver = self.driver
        driver.get(self.base_dev_url)

        login = LoginPage(driver)
        login.enter_tenant("priyanshu")
        login.enter_continue()
        login.enter_username("priyanshu")
        login.enter_password("password")
        login.click_login()

        dashboard = DashboardPage(driver)
        customer = AddCustomerPage(driver)
        time.sleep(3)
        dashboard.click_crm()
        dashboard.click_customers()
        time.sleep(1)
        text1 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/main[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]").text
        customer.enter_search_filter(text1)
        customer.enter_search_filter(Keys.BACKSPACE)
        customer.enter_search_filter(Keys.BACKSPACE)
        customer.enter_search_filter(Keys.ENTER)
        time.sleep(1)
        customer.click_filter_icon()
        customer.click_search_by_email()
        customer.click_search_by_contact_no()
        customer.click_search_by_name()
        time.sleep(1)
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        text2 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/main[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]").text

        if text2 in text1:
            print(f"Valid Customer Name:> {text1}.")
        else:
            print(f"Invalid Customer Name:> {text2}.")
        time.sleep(1)
        dashboard.click_account()
        time.sleep(2)
        dashboard.click_logout()
        time.sleep(2)

    def test_020_crm(self):
        driver = self.driver
        driver.get(self.base_dev_url)

        login = LoginPage(driver)
        login.enter_tenant("priyanshu")
        login.enter_continue()
        login.enter_username("priyanshu")
        login.enter_password("password")
        login.click_login()

        dashboard = DashboardPage(driver)
        customer = AddCustomerPage(driver)
        time.sleep(3)
        dashboard.click_crm()
        dashboard.click_customers()
        time.sleep(1)
        text1 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/main[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]").text
        customer.enter_search_filter(text1)
        time.sleep(1)
        customer.click_filter_icon()
        customer.click_search_by_email()
        customer.click_search_by_contact_no()
        customer.click_search_by_name()
        time.sleep(1)
        customer.click_search_by_customer_id()
        customer.click_search_by_email()
        customer.click_search_by_contact_no()
        customer.click_search_by_name()
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        text2 = driver.find_element(By.XPATH, "//div[@role='alert']").text
        popup_text = "Please select atleast one Filter !"
        if text2 in popup_text:
            print(f"Valid Alert:> {popup_text}.")
        else:
            print(f"Invalid Alert:> {text2}.")
        time.sleep(1)
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


