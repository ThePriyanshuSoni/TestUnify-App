from selenium import webdriver
import HtmlTestRunner
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest
from selenium.webdriver.common.alert import Alert
from UnifyNG.POM.Pages.Login.loginPage import LoginPage
from UnifyNG.POM.Pages.Dashboard.dashboardPage import DashboardPage
from UnifyNG.POM.Pages.NgCreator.addNgCreatorPage import AddNgCreatorPage
import string
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class TestNgCreator(unittest.TestCase):
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

    def test_001_ng_creator(self):
        driver = self.driver
        driver.get(self.base_dev_url)

        login = LoginPage(driver)
        login.enter_tenant("priyanshu")
        login.enter_continue()
        login.enter_username("priyanshu")
        login.enter_password("password")
        login.click_login()
        time.sleep(3)
        dashboard = DashboardPage(driver)
        dashboard.click_ng_creator()
        dashboard.click_add_new()

        creator = AddNgCreatorPage(driver)
        creator.enter_form_title(''.join(random.choices(string.ascii_lowercase, k=8)))
        creator.click_save_button()
        time.sleep(3)

        creator.click_text_form()
        time.sleep(2)
        creator.enter_text_field_name(''.join(random.choices(string.ascii_lowercase, k=8)))
        time.sleep(3)
        creator.enter_text_placeholder(''.join(random.choices(string.ascii_lowercase, k=8)))
        creator.enter_text_regex("abcdefghijklmnopqrstuvwxyz12345")
        creator.click_search_option()
        creator.click_mandatory()
        time.sleep(2)
        creator.click_save_button()
        time.sleep(3)


        creator.click_text_area_form()
        time.sleep(2)
        creator.enter_text_a_field_name(''.join(random.choices(string.ascii_lowercase, k=8)))
        time.sleep(3)
        creator.enter_text_a_placeholder(''.join(random.choices(string.ascii_lowercase, k=8)))
        creator.enter_text_a_regex("abcdefghijklmnopqrstuvwxyz12345")
        creator.click_search_option()
        creator.click_mandatory()
        time.sleep(2)
        creator.click_save_button()
        time.sleep(3)

        creator.click_email_form()
        time.sleep(2)
        creator.enter_email_field_name(''.join(random.choices(string.ascii_lowercase, k=8)))
        time.sleep(3)
        creator.enter_email_placeholder(''.join(random.choices(string.ascii_lowercase, k=8)))
        creator.enter_email_regex("abcdefghijklmnopqrstuvwxyz12345")
        creator.click_search_option()
        creator.click_mandatory()
        time.sleep(2)
        creator.click_save_button()
        time.sleep(3)

        creator.click_checkbox_form()
        time.sleep(2)
        creator.enter_checkbox_field_name(''.join(random.choices(string.ascii_lowercase, k=8)))
        time.sleep(2)
        creator.enter_checkbox_regex("abcdefghijklmnopqrstuvwxyz12345")
        creator.click_search_option()
        creator.click_mandatory()
        time.sleep(2)
        creator.click_save_button()
        time.sleep(3)

        creator.click_select_form()
        time.sleep(2)
        creator.enter_select_field_name(''.join(random.choices(string.ascii_lowercase, k=8)))
        time.sleep(2)
        creator.enter_select_regex("abcdefghijklmnopqrstuvwxyz12345")
        creator.click_search_option()
        creator.click_mandatory()
        time.sleep(2)
        creator.click_add_option()
        creator.enter_option()
        time.sleep(2)
        creator.click_save_button()
        time.sleep(3)

        creator.click_number_form()
        time.sleep(2)
        creator.enter_number_field_name(''.join(random.choices(string.ascii_lowercase, k=8)))
        time.sleep(3)
        creator.enter_number_placeholder(''.join(random.choices(string.ascii_lowercase, k=8)))
        creator.enter_number_regex("abcdefghijklmnopqrstuvwxyz12345")
        creator.click_search_option()
        creator.click_mandatory()
        time.sleep(2)
        creator.click_save_button()
        time.sleep(3)

        creator.click_date_form()
        time.sleep(2)
        creator.enter_date_field_name()
        time.sleep(3)
        creator.click_search_option()
        creator.click_mandatory()
        time.sleep(2)
        creator.click_save_button()
        time.sleep(3)

        creator.click_datetime_form()
        time.sleep(2)
        creator.enter_datetime_field_name()
        time.sleep(3)
        creator.click_search_option()
        creator.click_mandatory()
        time.sleep(2)
        creator.click_save_button()
        time.sleep(3)

        creator.click_sub_form()
        time.sleep(2)
        creator.enter_datetime_field_name()
        time.sleep(2)
        creator.click_save_button()
        time.sleep(3)
        dashboard.page_scroll_to_top()
        time.sleep(2)

        creator.click_preview()
        time.sleep(2)
        creator.click_save_button()
        time.sleep(2)
        creator.click_back_button()
        time.sleep(3)
        dashboard.click_account()
        time.sleep(2)
        dashboard.click_logout()
        time.sleep(2)

    def test_002_ng_creator(self):
        driver = self.driver
        driver.get(self.base_dev_url)

        login = LoginPage(driver)
        login.enter_tenant("priyanshu")
        login.enter_continue()
        login.enter_username("priyanshu")
        login.enter_password("password")
        login.click_login()
        time.sleep(3)
        dashboard = DashboardPage(driver)
        dashboard.click_ng_creator()
        dashboard.click_add_new()

        creator = AddNgCreatorPage(driver)
        creator.click_save_button()
        time.sleep(3)
        error = driver.find_element(By.XPATH, "//p[@id='formTitle-helper-text']").text
        popup_text = "Form Title cannot be blank!"
        if popup_text in error:
            print(f"Valid Error:> {popup_text}.")
        else:
            print(f"Invalid Error:> {error}.")
        creator.click_discard_button()
        time.sleep(3)
        dashboard.click_account()
        time.sleep(2)
        dashboard.click_logout()
        time.sleep(2)

    def test_003_ng_creator(self):
        driver = self.driver
        driver.get(self.base_dev_url)

        login = LoginPage(driver)
        login.enter_tenant("priyanshu")
        login.enter_continue()
        login.enter_username("priyanshu")
        login.enter_password("password")
        login.click_login()
        time.sleep(3)
        dashboard = DashboardPage(driver)
        dashboard.click_ng_creator()

        creator = AddNgCreatorPage(driver)
        creator.click_action_three_dot()
        creator.click_action_edit()
        time.sleep(2)
        creator.click_pencil_edit()
        time.sleep(2)
        creator.enter_text_field_name(''.join(random.choices(string.ascii_lowercase, k=8)))
        creator.click_save_button()
        time.sleep(2)
        creator.click_delete_icon()
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(2)
        creator.click_preview()
        time.sleep(2)
        creator.click_save_button()
        time.sleep(2)
        creator.click_back_button()
        dashboard.click_account()
        time.sleep(2)
        dashboard.click_logout()
        time.sleep(2)

    def test_004_ng_creator(self):
        driver = self.driver
        driver.get(self.base_dev_url)

        alert = Alert(driver)
        login = LoginPage(driver)
        login.enter_tenant("priyanshu")
        login.enter_continue()
        login.enter_username("priyanshu")
        login.enter_password("password")
        login.click_login()
        time.sleep(3)
        dashboard = DashboardPage(driver)
        dashboard.click_ng_creator()
        time.sleep(2)
        dashboard.click_add_new()

        creator = AddNgCreatorPage(driver)
        creator.enter_form_title(''.join(random.choices(string.ascii_lowercase, k=8)))
        creator.click_save_button()
        time.sleep(3)

        creator.click_sub_form()
        time.sleep(1)
        creator.enter_text_field_name("ng field name")
        time.sleep(1)
        creator.click_save_button()
        time.sleep(1)
        creator.click_select_field()
        time.sleep(1)
        creator.click_dropdown_text()
        creator.enter_text_field_name(''.join(random.choices(string.ascii_lowercase, k=8)))
        time.sleep(1)
        creator.enter_text_placeholder(''.join(random.choices(string.ascii_lowercase, k=8)))
        creator.enter_text_regex("abcdefghijklmnopqrstuvwxyz12345")
        creator.click_search_option()
        creator.click_mandatory()
        time.sleep(1)
        creator.click_save_button()
        time.sleep(1)
        dashboard.page_scroll_to_top()
        time.sleep(1)
        creator.click_back_button()
        time.sleep(1)
        creator.click_first_form_name()
        time.sleep(1)
        creator.click_add_data_button()
        time.sleep(1)
        creator.click_add_new_row()
        creator.enter_add_data_placeholder("add data created")
        time.sleep(1)
        creator.click_save_button_placeholder()
        time.sleep(1)
        creator.click_save_button()
        time.sleep(1)
        creator.click_back_button()
        time.sleep(2)
        creator.click_action_three_dot()
        time.sleep(1)
        creator.click_action_edit()
        time.sleep(1)
        creator.click_delete_icon()
        alert1 = alert.text
        popup_text = "Are you sure you want to delete?"
        if alert1 in popup_text:
            print(f"Valid Alert :> {popup_text}.")
        else:
            print(f"Invalid Alert :> {alert1}.")
        alert.accept()

        time.sleep(5)

        alert2 = driver.find_element(By.XPATH, "//div[@role='alert']").text
        popup_text = "Field Can't be deleted as it contains Data"
        if alert2 in popup_text:
            print(f"Valid Alert :> {popup_text}.")
        else:
            print(f"Invalid Alert :> {alert2}.")

        dashboard.click_account()
        time.sleep(1)
        dashboard.click_logout()
        time.sleep(2)

    def test_005_ng_creator(self):
        driver = self.driver
        driver.get(self.base_dev_url)

        login = LoginPage(driver)
        login.enter_tenant("priyanshu")
        login.enter_continue()
        login.enter_username("priyanshu")
        login.enter_password("password")
        login.click_login()
        time.sleep(3)

        dashboard = DashboardPage(driver)
        dashboard.click_ng_creator()
        creator = AddNgCreatorPage(driver)
        creator.click_action_three_dot()
        time.sleep(2)
        creator.click_action_delete()
        time.sleep(2)
        error = driver.find_element(By.XPATH, "//div[contains(text(),'Form deleted successfully')]").text
        popup_text = "Form deleted successfully"
        if error in popup_text:
            print(f"Valid Alert:> {popup_text}.")
        else:
            print(f"Invalid Alert:> {error}.")

        dashboard.click_account()
        time.sleep(2)
        dashboard.click_logout()
        time.sleep(2)

    def test_006_ng_creator(self):
        driver = self.driver
        driver.get(self.base_dev_url)

        login = LoginPage(driver)
        login.enter_tenant("priyanshu")
        login.enter_continue()
        login.enter_username("priyanshu")
        login.enter_password("password")
        login.click_login()
        time.sleep(3)
        dashboard = DashboardPage(driver)
        dashboard.click_ng_creator()
        time.sleep(2)
        dashboard.click_add_new()

        creator = AddNgCreatorPage(driver)
        creator.enter_form_title(''.join(random.choices(string.ascii_lowercase, k=8)))
        creator.click_save_button()
        time.sleep(3)

        creator.click_sub_form()
        time.sleep(1)
        creator.enter_text_field_name("ng field name")
        time.sleep(1)
        creator.click_save_button()
        time.sleep(1)
        creator.click_select_field()
        time.sleep(1)
        creator.click_dropdown_text()
        creator.enter_text_field_name(''.join(random.choices(string.ascii_lowercase, k=8)))
        time.sleep(1)
        creator.enter_text_placeholder(''.join(random.choices(string.ascii_lowercase, k=8)))
        creator.enter_text_regex("abcdefghijklmnopqrstuvwxyz12345")
        creator.click_search_option()
        creator.click_mandatory()
        time.sleep(1)
        creator.click_save_button()
        time.sleep(1)
        dashboard.page_scroll_to_top()
        time.sleep(1)
        creator.click_back_button()
        time.sleep(1)
        creator.click_first_form_name()
        time.sleep(1)
        creator.click_add_data_button()
        time.sleep(1)
        creator.click_add_new_row()
        creator.enter_add_data_placeholder("add data created")
        time.sleep(1)
        creator.click_save_button_placeholder()
        time.sleep(1)
        creator.click_save_button()
        time.sleep(1)
        creator.click_back_button()
        time.sleep(2)
        creator.click_action_three_dot()
        time.sleep(1)
        creator.click_action_delete()
        time.sleep(2)
        alert = driver.find_element(By.XPATH, "//div[@role='alert']").text
        popup_text = "Form can't be deleted as it contains data"
        if alert in popup_text:
            print(f"Valid Alert :> {popup_text}.")
        else:
            print(f"Invalid Alert :> {alert}.")

        dashboard.click_account()
        time.sleep(1)
        dashboard.click_logout()
        time.sleep(2)

    def test_007_ng_creator(self):
        driver = self.driver
        driver.get(self.base_dev_url)

        login = LoginPage(driver)
        login.enter_tenant("priyanshu")
        login.enter_continue()
        login.enter_username("priyanshu")
        login.enter_password("password")
        login.click_login()
        time.sleep(3)

        dashboard = DashboardPage(driver)
        dashboard.click_ng_creator()
        creator = AddNgCreatorPage(driver)
        creator.click_action_three_dot()
        time.sleep(2)
        creator.click_dot_rename_form()
        time.sleep(2)
        creator.enter_form_title(''.join(random.choices(string.ascii_lowercase, k=8)))
        time.sleep(2)
        creator.click_save_button()
        time.sleep(2)
        expected = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/main[1]/div[2]/div[1]/h5[1]").text
        error = driver.find_element(By.XPATH, "//div[contains(text(),'Form renamed successfully')]").text
        popup_text = "Form renamed successfully"
        if popup_text in error:
            print(f"Valid Alert:> {popup_text}.")
        else:
            print(f"Invalid Alert:> {error}.")
        creator.click_back_button()
        time.sleep(2)
        creator.click_first_form_name()
        time.sleep(2)
        actual = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/main[1]/div[2]/div[1]/h5[1]").text
        if actual in expected:
            print(f"\n Matched with the updated form name:> {actual}.")
        else:
            print(f"\n Doesn't Matched with the updated form name:> {expected}.")
        dashboard.click_account()
        time.sleep(2)
        dashboard.click_logout()
        time.sleep(2)

    def test_008_ng_creator(self):
        driver = self.driver
        driver.get(self.base_dev_url)

        login = LoginPage(driver)
        login.enter_tenant("priyanshu")
        login.enter_continue()
        login.enter_username("priyanshu")
        login.enter_password("password")
        login.click_login()
        time.sleep(3)

        dashboard = DashboardPage(driver)
        dashboard.click_ng_creator()
        creator = AddNgCreatorPage(driver)
        creator.click_action_three_dot()
        time.sleep(2)
        creator.click_dot_rename_form()
        time.sleep(2)
        creator.clear_form_title_backspace()
        time.sleep(2)
        creator.click_save_button()
        time.sleep(2)

        error = driver.find_element(By.XPATH, "//p[@id='formTitle-helper-text']").text
        popup_text = "Form Title cannot be blank!"
        if popup_text in error:
            print(f"Valid Error:> {popup_text}.")
        else:
            print(f"Invalid Error:> {error}.")

        creator.click_discard_button()
        dashboard.click_account()
        time.sleep(2)
        dashboard.click_logout()
        time.sleep(2)


    def test_009_ng_creator(self):
        driver = self.driver
        driver.get(self.base_dev_url)

        login = LoginPage(driver)
        login.enter_tenant("priyanshu")
        login.enter_continue()
        login.enter_username("priyanshu")
        login.enter_password("password")
        login.click_login()
        time.sleep(3)

        dashboard = DashboardPage(driver)
        dashboard.click_ng_creator()
        creator = AddNgCreatorPage(driver)
        creator.click_action_three_dot()
        time.sleep(2)
        creator.click_dot_export()
        time.sleep(2)

        error = driver.find_element(By.XPATH, "//div[contains(text(),'Downloaded successfully')]").text
        popup_text = "Downloaded successfully"
        if popup_text in error:
            print(f"Valid Alert:> {popup_text}.")
        else:
            print(f"Invalid Alert:> {error}.")

        dashboard.click_account()
        time.sleep(2)
        dashboard.click_logout()
        time.sleep(2)


    def test_010_ng_creator(self):
        driver = self.driver
        driver.get(self.base_dev_url)

        login = LoginPage(driver)
        login.enter_tenant("priyanshu")
        login.enter_continue()
        login.enter_username("priyanshu")
        login.enter_password("password")
        login.click_login()
        time.sleep(3)
        dashboard = DashboardPage(driver)
        dashboard.click_ng_creator()
        dashboard.click_add_new()

        creator = AddNgCreatorPage(driver)
        creator.enter_form_title(''.join(random.choices(string.ascii_lowercase, k=8)))
        creator.click_save_button()
        time.sleep(3)

        creator.click_text_form()
        time.sleep(2)
        creator.enter_text_field_name("ng field name")
        time.sleep(3)
        creator.enter_text_placeholder("ng placeholder")
        creator.enter_text_regex("abcdefghijklmnopqrstuvwxyz12345")
        time.sleep(1)
        creator.click_save_button()
        time.sleep(1)
        creator.click_preview()
        time.sleep(1)
        creator.click_save_button()
        time.sleep(1)
        creator.click_back_button()
        time.sleep(1)
        creator.click_first_form_name()
        time.sleep(2)
        creator.click_add_data_button()
        creator.enter_text_data(''.join(random.choices(string.ascii_lowercase, k=8)))
        creator.click_save_button()
        time.sleep(3)

        error = driver.find_element(By.XPATH, "//div[contains(text(),'Data added')]").text
        popup_text = "Data added successfully"
        if popup_text in error:
            print(f"Valid Alert without mandatory field:> {popup_text}.")
        else:
            print(f"Invalid Alert:> {error}.")

        creator.click_back_button()
        dashboard.click_account()
        time.sleep(2)
        dashboard.click_logout()
        time.sleep(2)


    def test_011_ng_creator(self):
        driver = self.driver
        driver.get(self.base_dev_url)

        login = LoginPage(driver)
        login.enter_tenant("priyanshu")
        login.enter_continue()
        login.enter_username("priyanshu")
        login.enter_password("password")
        login.click_login()
        time.sleep(3)
        dashboard = DashboardPage(driver)
        dashboard.click_ng_creator()
        dashboard.click_add_new()

        creator = AddNgCreatorPage(driver)
        creator.enter_form_title(''.join(random.choices(string.ascii_lowercase, k=8)))
        creator.click_save_button()
        time.sleep(3)

        creator.click_text_form()
        time.sleep(2)
        creator.enter_text_field_name("ng field name")
        time.sleep(3)
        creator.enter_text_placeholder("ng placeholder")
        creator.enter_text_regex("abcdefghijklmnopqrstuvwxyz12345")
        creator.click_search_option()
        creator.click_mandatory()
        time.sleep(1)
        creator.click_save_button()
        time.sleep(1)
        creator.click_preview()
        time.sleep(1)
        creator.click_save_button()
        time.sleep(1)
        creator.click_back_button()
        time.sleep(1)
        creator.click_first_form_name()
        time.sleep(2)
        creator.click_add_data_button()
        creator.enter_text_data(''.join(random.choices(string.ascii_lowercase, k=8)))
        creator.click_save_button()
        time.sleep(3)

        error = driver.find_element(By.XPATH, "//div[contains(text(),'Data added')]").text
        popup_text = "Data added successfully"
        if popup_text in error:
            print(f"Valid Alert with mandatory field:> {popup_text}.")
        else:
            print(f"Invalid Alert:> {error}.")

        creator.click_back_button()
        dashboard.click_account()
        time.sleep(2)
        dashboard.click_logout()
        time.sleep(2)

    def test_012_ng_creator(self):
        driver = self.driver
        driver.get(self.base_dev_url)

        login = LoginPage(driver)
        login.enter_tenant("priyanshu")
        login.enter_continue()
        login.enter_username("priyanshu")
        login.enter_password("password")
        login.click_login()
        time.sleep(3)
        dashboard = DashboardPage(driver)
        dashboard.click_ng_creator()
        dashboard.click_add_new()

        creator = AddNgCreatorPage(driver)
        creator.enter_form_title(''.join(random.choices(string.ascii_lowercase, k=8)))
        creator.click_save_button()
        time.sleep(3)

        creator.click_text_form()
        time.sleep(2)
        creator.enter_text_field_name("ng field name")
        time.sleep(3)
        creator.enter_text_placeholder("ng placeholder")
        creator.enter_text_regex("abcdefghijklmnopqrstuvwxyz12345")
        creator.click_search_option()
        creator.click_mandatory()
        time.sleep(1)
        creator.click_save_button()
        time.sleep(1)
        creator.click_preview()
        time.sleep(1)
        creator.click_save_button()
        time.sleep(1)
        creator.click_back_button()
        time.sleep(1)
        creator.click_first_form_name()
        time.sleep(1)
        creator.click_add_data_button()
        time.sleep(1)
        creator.click_save_button()
        time.sleep(3)

        error = driver.find_element(By.XPATH, "//div[contains(text(),'Please fill all the mandatory fields')]").text
        popup_text = "Please fill all the mandatory fields"
        if popup_text in error:
            print(f"Valid Alert with mandatory field:> {popup_text}.")
        else:
            print(f"Invalid Alert:> {error}.")

        creator.click_back_button()
        dashboard.click_account()
        time.sleep(2)
        dashboard.click_logout()
        time.sleep(2)

    def test_013_ng_creator(self):
        driver = self.driver
        driver.get(self.base_dev_url)
        wait = WebDriverWait(driver, 10)
        login = LoginPage(driver)
        login.enter_tenant("priyanshu")
        login.enter_continue()
        login.enter_username("priyanshu")
        login.enter_password("password")
        login.click_login()
        time.sleep(3)
        dashboard = DashboardPage(driver)
        dashboard.click_ng_creator()
        time.sleep(2)
        dashboard.click_add_new()

        creator = AddNgCreatorPage(driver)
        creator.enter_form_title(''.join(random.choices(string.ascii_lowercase, k=8)))
        creator.click_save_button()
        time.sleep(3)

        creator.click_sub_form()
        time.sleep(1)
        creator.enter_text_field_name("ng field name")
        time.sleep(1)
        creator.click_save_button()
        time.sleep(1)
        creator.click_select_field()
        time.sleep(1)
        creator.click_dropdown_text()
        creator.enter_text_field_name(''.join(random.choices(string.ascii_lowercase, k=8)))
        time.sleep(1)
        creator.enter_text_placeholder(''.join(random.choices(string.ascii_lowercase, k=8)))
        creator.enter_text_regex("abcdefghijklmnopqrstuvwxyz12345")
        time.sleep(1)
        creator.click_save_button()
        time.sleep(1)

        alert = driver.find_element(By.XPATH, "//div[contains(text(),'Sub Field added successfully')]").text
        popup_text = "Sub Field added successfully"
        if alert in popup_text:
            print(f"Valid Alert with without mandatory field:> {popup_text}.")
        else:
            print(f"Invalid Alert:> {alert}.")
        dashboard.page_scroll_to_top()
        time.sleep(1)
        creator.click_back_button()
        time.sleep(1)
        creator.click_first_form_name()
        time.sleep(1)
        creator.click_add_data_button()
        time.sleep(1)
        creator.click_add_new_row()
        creator.enter_add_data_placeholder("add data created")
        time.sleep(1)
        creator.click_save_button_placeholder()
        time.sleep(2)
        creator.click_back_button()
        time.sleep(1)
        dashboard.click_account()
        time.sleep(1)
        dashboard.click_logout()
        time.sleep(2)

    def test_014_ng_creator(self):
        driver = self.driver
        driver.get(self.base_dev_url)
        wait = WebDriverWait(driver, 10)
        login = LoginPage(driver)
        login.enter_tenant("priyanshu")
        login.enter_continue()
        login.enter_username("priyanshu")
        login.enter_password("password")
        login.click_login()
        time.sleep(3)
        dashboard = DashboardPage(driver)
        dashboard.click_ng_creator()
        time.sleep(2)
        dashboard.click_add_new()

        creator = AddNgCreatorPage(driver)
        creator.enter_form_title(''.join(random.choices(string.ascii_lowercase, k=8)))
        creator.click_save_button()
        time.sleep(3)

        creator.click_sub_form()
        time.sleep(1)
        creator.enter_text_field_name("ng field name")
        time.sleep(1)
        creator.click_save_button()
        time.sleep(1)
        creator.click_select_field()
        time.sleep(1)
        creator.click_dropdown_text()
        creator.enter_text_field_name(''.join(random.choices(string.ascii_lowercase, k=8)))
        time.sleep(1)
        creator.enter_text_placeholder(''.join(random.choices(string.ascii_lowercase, k=8)))
        creator.enter_text_regex("abcdefghijklmnopqrstuvwxyz12345")
        creator.click_search_option()
        creator.click_mandatory()
        time.sleep(1)
        creator.click_save_button()
        time.sleep(1)

        alert1 = driver.find_element(By.XPATH, "//div[contains(text(),'Sub Field added successfully')]").text
        popup_text = "Sub Field added successfully"
        if alert1 in popup_text:
            print(f"Valid Alert with with mandatory field:> {popup_text}.")
        else:
            print(f"Invalid Alert:> {alert1}.")
        dashboard.page_scroll_to_top()
        time.sleep(1)
        creator.click_back_button()
        time.sleep(1)
        creator.click_first_form_name()
        time.sleep(1)
        creator.click_add_data_button()
        time.sleep(1)
        creator.click_add_new_row()
        creator.enter_add_data_placeholder("add data created")
        time.sleep(1)
        creator.click_save_button_placeholder()
        time.sleep(1)
        creator.click_save_button()
        time.sleep(1)
        alert2 = driver.find_element(By.XPATH, "//div[@role='alert']").text
        popup_text = "data added successfully"
        if alert2 in popup_text:
            print(f"Valid Alert with with mandatory field:> {popup_text}.")
        else:
            print(f"Invalid Alert:> {alert2}.")
        creator.click_back_button()
        time.sleep(1)
        dashboard.click_account()
        time.sleep(1)
        dashboard.click_logout()
        time.sleep(2)


    def test_015_ng_creator(self):
        driver = self.driver
        driver.get(self.base_dev_url)
        login = LoginPage(driver)
        login.enter_tenant("priyanshu")
        login.enter_continue()
        login.enter_username("priyanshu")
        login.enter_password("password")
        login.click_login()
        time.sleep(3)
        dashboard = DashboardPage(driver)
        dashboard.click_ng_creator()
        time.sleep(2)
        dashboard.click_add_new()

        creator = AddNgCreatorPage(driver)
        creator.enter_form_title(''.join(random.choices(string.ascii_lowercase, k=8)))
        creator.click_save_button()
        time.sleep(3)

        creator.click_sub_form()
        time.sleep(1)
        creator.enter_text_field_name("ng field name")
        time.sleep(1)
        creator.click_save_button()
        time.sleep(1)
        creator.click_select_field()
        time.sleep(1)
        creator.click_dropdown_text()
        creator.enter_text_field_name(''.join(random.choices(string.ascii_lowercase, k=8)))
        time.sleep(1)
        creator.enter_text_placeholder(''.join(random.choices(string.ascii_lowercase, k=8)))
        creator.enter_text_regex("abcdefghijklmnopqrstuvwxyz12345")
        creator.click_search_option()
        creator.click_mandatory()
        time.sleep(1)
        creator.click_save_button()
        time.sleep(1)

        alert1 = driver.find_element(By.XPATH, "//div[contains(text(),'Sub Field added successfully')]").text
        popup_text = "Sub Field added successfully"
        if alert1 in popup_text:
            print(f"Valid Alert with with mandatory field:> {popup_text}.")
        else:
            print(f"Invalid Alert:> {alert1}.")
        dashboard.page_scroll_to_top()
        time.sleep(1)
        creator.click_back_button()
        time.sleep(1)
        creator.click_first_form_name()
        time.sleep(1)
        creator.click_add_data_button()
        time.sleep(1)
        creator.click_add_new_row()
        time.sleep(1)
        creator.click_save_button_placeholder()
        time.sleep(1)
        creator.click_close_button_icon()
        creator.click_save_button()
        time.sleep(1)
        alert2 = driver.find_element(By.XPATH, "//div[@role='alert']").text
        popup_text = "Please fill the mandatory fields"
        if alert2 in popup_text:
            print(f"Valid Alert with with mandatory field:> {popup_text}.")
        else:
            print(f"Invalid Alert:> {alert2}.")
        creator.click_back_button()
        time.sleep(1)
        dashboard.click_account()
        time.sleep(1)
        dashboard.click_logout()
        time.sleep(2)


    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()



n = 7
name = ''.join(random.choices(string.ascii_uppercase, k=n))
pb = str(name)


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/home/priyansu/Desktop/testing/unifyng-automation-testing/UnifyNG/Reports"))

