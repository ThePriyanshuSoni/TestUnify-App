from selenium import webdriver
import HtmlTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from faker import Faker
import time
import unittest
from UnifyNG.POM.Pages.Login.loginPage import LoginPage
from UnifyNG.POM.Pages.Dashboard.dashboardPage import DashboardPage
from UnifyNG.POM.Pages.TaxConfiguration.addTaxProfilePage import AddTaxProfilePage



fake = Faker(['en_US'])
fake_word = fake.word()


class AddTaxProfile(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    # def test_001_tax(self):
    #     driver = self.driver
    #     driver.get("http://unifyng.inventum.co/login")
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
    #     dashboard.click_tax_configuration()
    #     time.sleep(1)
    #     tprofile = AddTaxProfilePage(driver)
    #     tprofile.click_add_tax_profile()
    #     tprofile.enter_profile_name(fake_word)
    #     tprofile.click_save()
    #     time.sleep(1)
    #     text = driver.find_element(By.XPATH, "//div[@role='alert']").text
    #     popup_text = "Tax Profile added successfully"
    #     if text in popup_text:
    #         print(f"Valid Alert:> {popup_text}.")
    #     else:
    #         print(f"Invalid Alert:> {text}.")
    #     time.sleep(1)
    #     dashboard.click_account()
    #     time.sleep(2)
    #     dashboard.click_logout()
    #     time.sleep(2)

    # def test_002_tax(self):
    #     driver = self.driver
    #     driver.get("http://unifyng.inventum.co/login")
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
    #     dashboard.click_tax_configuration()
    #     time.sleep(1)
    #     tprofile = AddTaxProfilePage(driver)
    #     tprofile.click_add_tax_profile()
    #     tprofile.click_save()
    #     time.sleep(1)
    #     text = driver.find_element(By.XPATH, "//p[@id='tax_profile_name-helper-text']").text
    #     webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    #     popup_text = "Profile name cannot be blank!"
    #     if text in popup_text:
    #         print(f"Valid Alert:> {popup_text}.")
    #     else:
    #         print(f"Invalid Alert:> {text}.")
    #     time.sleep(1)
    #     dashboard.click_account()
    #     time.sleep(2)
    #     dashboard.click_logout()
    #     time.sleep(2)

    # def test_003_tax(self):
    #     driver = self.driver
    #     driver.get("http://unifyng.inventum.co/login")
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
    #     dashboard.click_tax_configuration()
    #     time.sleep(1)
    #     tprofile = AddTaxProfilePage(driver)
    #     tprofile.click_add_tax_profile()
    #     tprofile.enter_profile_name(fake_word)
    #     tprofile.click_save()
    #     time.sleep(2)
    #     tprofile.click_settings_icon()
    #     time.sleep(1)
    #     tprofile.enter_label("Internet")
    #     tprofile.enter_sgst("9")
    #     tprofile.enter_cgst("9")
    #     time.sleep(2)
    #     tprofile.click_save()
    #     time.sleep(1)
    #     text = driver.find_element(By.XPATH, "//div[@role='alert']").text
    #     popup_text = "Tax Configuration updated successfully!"
    #     if text in popup_text:
    #         print(f"Valid Alert:> {popup_text}.")
    #     else:
    #         print(f"Invalid Alert:> {text}.")
    #     tprofile.click_back()
    #     time.sleep(1)
    #     dashboard.click_account()
    #     time.sleep(2)
    #     dashboard.click_logout()

    # def test_004_tax(self):
    #     driver = self.driver
    #     driver.get("http://unifyng.inventum.co/login")
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
    #     dashboard.click_tax_configuration()
    #     time.sleep(1)
    #     tprofile = AddTaxProfilePage(driver)
    #     tprofile.click_add_tax_profile()
    #     tprofile.enter_profile_name(fake_word)
    #     tprofile.click_save()
    #     time.sleep(2)
    #     tprofile.click_settings_icon()
    #     tprofile.click_manual_type()
    #     time.sleep(1)
    #     tprofile.enter_label("VAT")
    #     tprofile.enter_add_tax_rate("18")
    #     time.sleep(2)
    #     tprofile.click_save()
    #     time.sleep(1)
    #     text = driver.find_element(By.XPATH, "//div[@role='alert']").text
    #     popup_text = "Tax Configuration updated successfully!"
    #     if text in popup_text:
    #         print(f"Valid Alert:> {popup_text}.")
    #     else:
    #         print(f"Invalid Alert:> {text}.")
    #     tprofile.click_back()
    #     time.sleep(1)
    #     dashboard.click_account()
    #     time.sleep(2)
    #     dashboard.click_logout()

    # def test_007_tax(self):
    #     driver = self.driver
    #     driver.get("http://unifyng.inventum.co/login")
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
    #     dashboard.click_tax_configuration()
    #     time.sleep(1)
    #     tprofile = AddTaxProfilePage(driver)
    #     tprofile.click_add_tax_profile()
    #     tprofile.enter_profile_name(fake_word)
    #     tprofile.click_save()
    #     time.sleep(2)
    #     tprofile.click_settings_icon()
    #     time.sleep(1)
    #     tprofile.click_save()
    #     time.sleep(1)
    #
    #     label = driver.find_element(By.ID, "label-helper-text").text
    #     popup_label = "Label cannot be blank!"
    #     if label in popup_label:
    #         print(f"Valid Alert:> {popup_label}.")
    #     else:
    #         print(f"Invalid Alert:> {label}.")
    #
    #     cgst = driver.find_element(By.ID, "sgst_ugst-helper-text").text
    #     popup_cgst = "SGST cannot be blank!"
    #     if cgst in popup_cgst:
    #         print(f"Valid Alert:> {popup_cgst}.")
    #     else:
    #         print(f"Invalid Alert:> {cgst}.")
    #
    #     sgst = driver.find_element(By.ID, "cgst-helper-text").text
    #     popup_sgst = "CGST cannot be blank!"
    #     if sgst in popup_sgst:
    #         print(f"Valid Alert:> {popup_sgst}.")
    #     else:
    #         print(f"Invalid Alert:> {sgst}.")
    #
    #     tprofile.click_back()
    #     time.sleep(1)
    #     dashboard.click_account()
    #     time.sleep(2)
    #     dashboard.click_logout()


    def test_008_tax(self):
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
        dashboard.click_tax_configuration()
        time.sleep(1)
        tprofile = AddTaxProfilePage(driver)
        tprofile.click_add_tax_profile()
        tprofile.enter_profile_name(fake_word)
        tprofile.click_save()
        time.sleep(2)
        tprofile.click_settings_icon()
        time.sleep(1)
        tprofile.click_manual_type()
        tprofile.click_save()
        time.sleep(1)

        label = driver.find_element(By.ID, "label-helper-text").text
        popup_label = "Label cannot be blank!"
        if label in popup_label:
            print(f"Valid Alert:> {popup_label}.")
        else:
            print(f"Invalid Alert:> {label}.")

        taxrate = driver.find_element(By.ID, "tax_rate-helper-text").text
        popup_cgst = "Add Tax Rate cannot be blank!"
        if taxrate in popup_cgst:
            print(f"Valid Alert:> {popup_cgst}.")
        else:
            print(f"Invalid Alert:> {taxrate}.")

        tprofile.click_back()
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


