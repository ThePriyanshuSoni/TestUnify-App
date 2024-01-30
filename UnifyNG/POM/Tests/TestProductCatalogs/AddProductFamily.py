import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest
from faker import Faker
from UnifyNG.POM.Pages.Login.loginPage import LoginPage
from UnifyNG.POM.Pages.Dashboard.dashboardPage import DashboardPage
from UnifyNG.POM.Pages.ProductCatalogs.Product.addProductPage import AddProductPage
from UnifyNG.POM.Pages.ProductCatalogs.ProductFamilies.addProductFamilyPage import AddProductFamilyPage



fake = Faker(['en_US'])
product_family = fake.street_name()
description = fake.sentence(nb_words=10)
name = fake.name()



class AddProductFamily(unittest.TestCase):
    url = "https://testunifyng.inventum.co/login"
    # base_dev_url = "https://unifyng.inventum.co/login"
    # base_test_url = "https://testunifyng.inventum.co/login"
    # priyanshu_tenant = "https://priyanshu.inventum.co/"
    tenant_username = "k"
    password = "password"

    @classmethod
    def setUp(cls):
        chrome_options = Options()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--disable-gpu')
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    def test_001_catalog(self):
        driver = self.driver
        driver.get(self.url)

        login = LoginPage(driver)
        login.enter_tenant(self.tenant_username)
        login.click_continue()
        login.enter_username(self.tenant_username)
        login.enter_password(self.password)
        login.click_login()
        time.sleep(2)

        dashboard = DashboardPage(driver)
        dashboard.click_product_catalogs()
        dashboard.click_product_families()
        time.sleep(2)

        family = AddProductFamilyPage(driver)
        family.click_add_product_family()
        family.enter_product_family_name(product_family)
        family.enter_description(description)
        family.click_save()
        time.sleep(1)
        text = driver.find_element(By.XPATH, "//div[@role='alert']").text
        popup_text = "Product Family added successfully"
        if text in popup_text:
            print(f"Valid Alert:> {popup_text}.")
        else:
            print(f"Invalid Alert:> {text}.")
        time.sleep(1)
        dashboard.click_account()
        time.sleep(2)
        dashboard.click_logout()


    def test_002_catalog(self):
        driver = self.driver
        driver.get(self.url)

        login = LoginPage(driver)
        login.enter_tenant(self.tenant_username)
        login.click_continue()
        login.enter_username(self.tenant_username)
        login.enter_password(self.password)
        login.click_login()
        time.sleep(2)

        dashboard = DashboardPage(driver)
        dashboard.click_product_catalogs()
        dashboard.click_product_families()
        time.sleep(2)

        family = AddProductFamilyPage(driver)
        family.click_add_product_family()
        family.click_save()
        time.sleep(1)
        text = driver.find_element(By.XPATH, "//p[@id='product_family_name-helper-text']").text
        popup_text = "product family cannot be blank!"
        if text in popup_text:
            print(f"Valid Alert:> {popup_text}.")
        else:
            print(f"Invalid Alert:> {text}.")
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        time.sleep(1)
        dashboard.click_account()
        time.sleep(2)
        dashboard.click_logout()


    def test_003_catalog(self):
        driver = self.driver
        driver.get(self.url)

        login = LoginPage(driver)
        login.enter_tenant(self.tenant_username)
        login.click_continue()
        login.enter_username(self.tenant_username)
        login.enter_password(self.password)
        login.click_login()
        time.sleep(2)

        dashboard = DashboardPage(driver)
        dashboard.click_product_catalogs()
        dashboard.click_product_families()
        time.sleep(2)

        family = AddProductFamilyPage(driver)
        family.click_add_product_family()
        family.enter_product_family_name("Internet-24")
        family.click_save()
        time.sleep(1)
        text = driver.find_element(By.XPATH, "//div[@role='alert']").text
        popup_text = "Product family name must be alphanumeric and can contain space and underscore"
        if text in popup_text:
            print(f"Valid Alert:> {popup_text}.")
        else:
            print(f"Invalid Alert:> {text}.")
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        time.sleep(1)
        dashboard.click_account()
        time.sleep(2)
        dashboard.click_logout()


    def test_004_catalog(self):
        driver = self.driver
        driver.get(self.url)

        login = LoginPage(driver)
        login.enter_tenant(self.tenant_username)
        login.click_continue()
        login.enter_username(self.tenant_username)
        login.enter_password(self.password)
        login.click_login()
        time.sleep(2)

        dashboard = DashboardPage(driver)
        dashboard.click_product_catalogs()
        dashboard.click_product_families()
        time.sleep(2)

        family = AddProductFamilyPage(driver)
        family.click_action_three_dot()
        family.click_action_edit()
        family.enter_product_family_name(Keys.CONTROL + "a")
        family.enter_product_family_name(Keys.BACKSPACE)
        family.enter_product_family_name("Internet_24")
        family.click_save()
        time.sleep(1)
        text = driver.find_element(By.XPATH, "//div[@role='alert']").text
        popup_text = "Product Family updated successfully"
        if text in popup_text:
            print(f"Valid Alert:> {popup_text}.")
        else:
            print(f"Invalid Alert:> {text}.")
        time.sleep(1)
        dashboard.click_account()
        time.sleep(2)
        dashboard.click_logout()


    def test_005_catalog(self):
        driver = self.driver
        driver.get(self.url)

        login = LoginPage(driver)
        login.enter_tenant(self.tenant_username)
        login.click_continue()
        login.enter_username(self.tenant_username)
        login.enter_password(self.password)
        login.click_login()
        time.sleep(2)

        dashboard = DashboardPage(driver)
        dashboard.click_product_catalogs()
        dashboard.click_product_families()
        time.sleep(2)

        family = AddProductFamilyPage(driver)
        # family.click_add_product_family()
        # family.enter_product_family_name(product_family)
        # family.enter_description(description)
        # family.click_save()
        # time.sleep(1)
        family.click_action_three_dot()
        family.click_action_delete()
        time.sleep(1)
        confirm_text = driver.find_element(By.XPATH, "//p[@class='MuiTypography-root MuiTypography-body1 MuiTypography-gutterBottom css-o9hva5-MuiTypography-root']").text
        family.enter_delete_product_name(confirm_text)
        time.sleep(1)
        family.click_are_you_about_to_delete()
        time.sleep(1)
        text = driver.find_element(By.XPATH, "//div[@role='alert']").text
        popup_text = "Product family deleted successfully"
        if text in popup_text:
            print(f"Valid Alert:> {popup_text}.")
        else:
            print(f"Invalid Alert:> {text}.")
        time.sleep(1)
        dashboard.click_account()
        time.sleep(2)
        dashboard.click_logout()


    def test_007_catalog(self):
        driver = self.driver
        driver.get(self.url)

        login = LoginPage(driver)
        login.enter_tenant(self.tenant_username)
        login.click_continue()
        login.enter_username(self.tenant_username)
        login.enter_password(self.password)
        login.click_login()
        time.sleep(2)

        dashboard = DashboardPage(driver)
        dashboard.click_product_catalogs()
        dashboard.click_product()

        product = AddProductPage(driver)
        product.click_add_product()
        product.click_product_family()
        product.select_product_family()
        product.enter_product_name(name)
        product.enter_description_name(description)
        time.sleep(1)
        # product.click_select_service()
        # product.select_service()
        # product.enter_service_plan_id("64f6eaf4d8319a4fa6014cbe")
        # product.click_validate()
        product.click_radio_recent_usage()
        time.sleep(1)
        # product.click_enable_webhook_toggle()
        # time.sleep(2)
        # driver.execute_script("scrollBy(0,300);")
        # time.sleep(5)
        product.click_save_button()

        time.sleep(1)
        text = driver.find_element(By.XPATH, "//div[@role='alert']").text
        popup_text = "Product added successfully"

        if text in popup_text:
            print(f"Valid Alert:> {popup_text}.")
        else:
            print(f"Invalid Alert:> {text}.")
        time.sleep(1)
        dashboard.click_account()
        time.sleep(2)
        dashboard.click_logout()


    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()



if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/home/priyansu/Desktop/testing/unifyng-automation-testing/UnifyNG/Reports"))
