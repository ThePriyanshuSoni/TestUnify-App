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
    base_dev_url = "http://unifyng.inventum.co/login"
    priyanshu_tenant = "http://priyanshu.inventum.co/"

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    # def test_001_tax(self):
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
    #
    # def test_002_tax(self):
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
    #
    # def test_003_tax(self):
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
    #
    # def test_004_tax(self):
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
    #
    # def test_007_tax(self):
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
    #     sgst = driver.find_element(By.ID, "sgst_ugst-helper-text").text
    #     popup_sgst = "SGST cannot be blank!"
    #     if sgst in popup_sgst:
    #         print(f"Valid Alert:> {popup_sgst}.")
    #     else:
    #         print(f"Invalid Alert:> {sgst}.")
    #
    #     cgst = driver.find_element(By.ID, "cgst-helper-text").text
    #     popup_cgst = "CGST cannot be blank!"
    #     if cgst in popup_cgst:
    #         print(f"Valid Alert:> {popup_cgst}.")
    #     else:
    #         print(f"Invalid Alert:> {cgst}.")
    #
    #     tprofile.click_back()
    #     time.sleep(1)
    #     dashboard.click_account()
    #     time.sleep(2)
    #     dashboard.click_logout()
    #
    #
    # def test_008_tax(self):
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
    #     dashboard.click_tax_configuration()
    #     time.sleep(1)
    #     tprofile = AddTaxProfilePage(driver)
    #     tprofile.click_add_tax_profile()
    #     tprofile.enter_profile_name(fake_word)
    #     tprofile.click_save()
    #     time.sleep(2)
    #     tprofile.click_settings_icon()
    #     time.sleep(1)
    #     tprofile.click_manual_type()
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
    #     taxrate = driver.find_element(By.ID, "tax_rate-helper-text").text
    #     popup_cgst = "Add Tax Rate cannot be blank!"
    #     if taxrate in popup_cgst:
    #         print(f"Valid Alert:> {popup_cgst}.")
    #     else:
    #         print(f"Invalid Alert:> {taxrate}.")
    #
    #     tprofile.click_back()
    #     time.sleep(1)
    #     dashboard.click_account()
    #     time.sleep(2)
    #     dashboard.click_logout()
    #
    #
    # def test_009_tax(self):
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
    #     dashboard.click_tax_configuration()
    #     time.sleep(1)
    #     tprofile = AddTaxProfilePage(driver)
    #     tprofile.click_add_tax_profile()
    #     tprofile.enter_profile_name(fake_word)
    #     tprofile.click_save()
    #     time.sleep(2)
    #     tprofile.click_settings_icon()
    #     tprofile.enter_label("label field")
    #     tprofile.enter_sgst("101")
    #     tprofile.enter_cgst("101")
    #     tprofile.enter_cess("101")
    #     time.sleep(1)
    #     dashboard.page_scroll_to_top()
    #     tprofile.click_save()
    #     time.sleep(1)
    #     text = driver.find_element(By.XPATH, "//div[@role='alert']").text
    #     popup_text = "cgst must not be higher than 100.00"
    #     if text in popup_text:
    #         print(f"Valid Alert:> {popup_text}.")
    #     else:
    #         print(f"Invalid Alert:> {text}.")
    #
    #     tprofile.click_back()
    #     time.sleep(1)
    #     dashboard.click_account()
    #     time.sleep(2)
    #     dashboard.click_logout()
    #
    #
    # def test_010_tax(self):
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
    #     dashboard.click_tax_configuration()
    #     time.sleep(1)
    #     tprofile = AddTaxProfilePage(driver)
    #     tprofile.click_add_tax_profile()
    #     tprofile.enter_profile_name(fake_word)
    #     tprofile.click_save()
    #     time.sleep(2)
    #     tprofile.click_settings_icon()
    #     tprofile.enter_label("label field")
    #     tprofile.enter_sgst("-5")
    #     tprofile.enter_cgst("-10")
    #     tprofile.enter_cess("-15")
    #     time.sleep(2)
    #     dashboard.page_scroll_to_top()
    #     tprofile.click_save()
    #     time.sleep(1)
    #     text = driver.find_element(By.XPATH, "//div[@role='alert']").text
    #     popup_text = "cgst must not be less than 0.0"
    #     if text in popup_text:
    #         print(f"Valid Alert:> {popup_text}.")
    #     else:
    #         print(f"Invalid Alert:> {text}.")
    #     tprofile.click_back()
    #
    #     time.sleep(1)
    #     dashboard.click_account()
    #     time.sleep(2)
    #     dashboard.click_logout()
    #
    #
    # def test_011_tax(self):
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
    #     dashboard.click_tax_configuration()
    #     time.sleep(1)
    #     tprofile = AddTaxProfilePage(driver)
    #     tprofile.click_add_tax_profile()
    #     tprofile.enter_profile_name(fake_word)
    #     tprofile.click_save()
    #     time.sleep(2)
    #     tprofile.click_settings_icon()
    #     time.sleep(2)
    #     tprofile.click_manual_type()
    #     tprofile.enter_label("manual label")
    #     tprofile.enter_add_tax_rate("105")
    #     tprofile.click_save()
    #     time.sleep(2)
    #
    #     text = driver.find_element(By.XPATH, "//div[@role='alert']").text
    #     popup_label = "tax_rate must not be higher than 100.00"
    #     if text in popup_label:
    #         print(f"Valid Alert:> {popup_label}.")
    #     else:
    #         print(f"Invalid Alert:> {text}.")
    #
    #     tprofile.click_back()
    #     time.sleep(1)
    #     dashboard.click_account()
    #     time.sleep(2)
    #     dashboard.click_logout()
    #
    #
    # def test_012_tax(self):
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
    #     dashboard.click_tax_configuration()
    #     time.sleep(1)
    #     tprofile = AddTaxProfilePage(driver)
    #     tprofile.click_add_tax_profile()
    #     tprofile.enter_profile_name(fake_word)
    #     tprofile.click_save()
    #     time.sleep(2)
    #     tprofile.click_settings_icon()
    #     time.sleep(2)
    #     tprofile.click_manual_type()
    #     tprofile.enter_label("manual label")
    #     tprofile.enter_add_tax_rate("-5")
    #     tprofile.click_save()
    #     time.sleep(2)
    #
    #     text = driver.find_element(By.XPATH, "//div[@role='alert']").text
    #     popup_label = "tax_rate must not be less than 0.0"
    #     if text in popup_label:
    #         print(f"Valid Alert:> {popup_label}.")
    #     else:
    #         print(f"Invalid Alert:> {text}.")
    #
    #     tprofile.click_back()
    #     time.sleep(1)
    #     dashboard.click_account()
    #     time.sleep(2)
    #     dashboard.click_logout()
    #
    #
    # def test_013_tax(self):
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
    #     dashboard.click_tax_configuration()
    #     time.sleep(1)
    #     tprofile = AddTaxProfilePage(driver)
    #     tprofile.click_add_tax_profile()
    #     tprofile.enter_profile_name(fake_word)
    #     tprofile.click_save()
    #     time.sleep(2)
    #     tprofile.click_settings_icon()
    #     time.sleep(1)
    #     dashboard.page_scroll_to_bottom()
    #     tprofile.click_add_state_tax_config()
    #     time.sleep(1)
    #     tprofile.click_save_state()
    #     time.sleep(1)
    #
    #     biller = driver.find_element(By.XPATH, "//p[@class='MuiFormHelperText-root MuiFormHelperText-sizeSmall MuiFormHelperText-contained error css-1l18pnj-MuiFormHelperText-root']").text
    #     popup_biller = "Please select biller"
    #     if biller in popup_biller:
    #         print(f"Valid Alert:> {popup_biller}.")
    #     else:
    #         print(f"Invalid Alert:> {biller}.")
    #
    #     label = driver.find_element(By.ID, "state_label-helper-text").text
    #     popup_label = "Label cannot be blank!"
    #     if label in popup_label:
    #         print(f"Valid Alert:> {popup_label}.")
    #     else:
    #         print(f"Invalid Alert:> {label}.")
    #
    #     sgst = driver.find_element(By.ID, "state_sgst_ugst-helper-text").text
    #     popup_sgst = "SGST cannot be blank!"
    #     if sgst in popup_sgst:
    #         print(f"Valid Alert:> {popup_sgst}.")
    #     else:
    #         print(f"Invalid Alert:> {sgst}.")
    #
    #     cgst = driver.find_element(By.ID, "state_cgst-helper-text").text
    #     popup_cgst = "CGST cannot be blank!"
    #     if cgst in popup_cgst:
    #         print(f"Valid Alert:> {popup_cgst}.")
    #     else:
    #         print(f"Invalid Alert:> {cgst}.")
    #
    #     webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    #     dashboard.page_scroll_to_top()
    #     tprofile.click_back()
    #     time.sleep(1)
    #     dashboard.click_account()
    #     time.sleep(2)
    #     dashboard.click_logout()
    #
    #
    # def test_014_tax(self):
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
    #     dashboard.click_tax_configuration()
    #     time.sleep(1)
    #     tprofile = AddTaxProfilePage(driver)
    #     tprofile.click_add_tax_profile()
    #     tprofile.enter_profile_name(fake_word)
    #     tprofile.click_save()
    #     time.sleep(2)
    #     tprofile.click_settings_icon()
    #     time.sleep(1)
    #     tprofile.click_manual_type()
    #     dashboard.page_scroll_to_bottom()
    #     tprofile.click_add_state_tax_config()
    #     time.sleep(1)
    #     tprofile.click_save_state()
    #     time.sleep(1)
    #
    #     biller = driver.find_element(By.XPATH, "//p[@class='MuiFormHelperText-root MuiFormHelperText-sizeSmall MuiFormHelperText-contained error css-1l18pnj-MuiFormHelperText-root']").text
    #     popup_biller = "Please select biller"
    #     if biller in popup_biller:
    #         print(f"Valid Alert:> {popup_biller}.")
    #     else:
    #         print(f"Invalid Alert:> {biller}.")
    #
    #     label = driver.find_element(By.ID, "state_label-helper-text").text
    #     popup_label = "Label cannot be blank!"
    #     if label in popup_label:
    #         print(f"Valid Alert:> {popup_label}.")
    #     else:
    #         print(f"Invalid Alert:> {label}.")
    #
    #     tax_rate = driver.find_element(By.ID, "state_tax_rate-helper-text").text
    #     popup_tax_rate = "Add Tax Rate cannot be blank!"
    #     if tax_rate in popup_tax_rate:
    #         print(f"Valid Alert:> {popup_tax_rate}.")
    #     else:
    #         print(f"Invalid Alert:> {tax_rate}.")
    #
    #     webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    #     dashboard.page_scroll_to_top()
    #     tprofile.click_back()
    #     time.sleep(1)
    #     dashboard.click_account()
    #     time.sleep(2)
    #     dashboard.click_logout()


    # def test_015_tax(self):
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
    #     dashboard.click_tax_configuration()
    #     time.sleep(1)
    #     tprofile = AddTaxProfilePage(driver)
    #     tprofile.click_add_tax_profile()
    #     tprofile.enter_profile_name(fake_word)
    #     tprofile.click_save()
    #     time.sleep(2)
    #     tprofile.click_settings_icon()
    #     time.sleep(1)
    #     dashboard.page_scroll_to_bottom()
    #     tprofile.click_add_state_tax_config()
    #     time.sleep(1)
    #     tprofile.click_state_biller()
    #     time.sleep(1)
    #     webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    #     time.sleep(1)
    #     tprofile.click_state_biller()
    #     time.sleep(1)
    #     webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
    #     time.sleep(4)
    #     tprofile.enter_state_label("tax label")
    #     tprofile.enter_state_sgst("101")
    #     tprofile.enter_state_cgst("101")
    #     tprofile.enter_state_cess("101")
    #
    #     tprofile.click_save_state()
    #     time.sleep(1)
    #
    #     text = driver.find_element(By.XPATH, "//div[@role='alert']").text
    #     popup = "cess must not be higher than 100.00"
    #     if text in popup:
    #         print(f"Valid Alert:> {popup}.")
    #     else:
    #         print(f"Invalid Alert:> {text}.")
    #
    #     webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    #     dashboard.page_scroll_to_top()
    #     tprofile.click_back()
    #     time.sleep(1)
    #     dashboard.click_account()
    #     time.sleep(2)
    #     dashboard.click_logout()


    # def test_016_tax(self):
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
    #     dashboard.click_tax_configuration()
    #     time.sleep(1)
    #     tprofile = AddTaxProfilePage(driver)
    #     tprofile.click_add_tax_profile()
    #     tprofile.enter_profile_name(fake_word)
    #     tprofile.click_save()
    #     time.sleep(2)
    #     tprofile.click_settings_icon()
    #     time.sleep(1)
    #     dashboard.page_scroll_to_bottom()
    #     tprofile.click_add_state_tax_config()
    #     time.sleep(1)
    #     tprofile.click_state_biller()
    #     time.sleep(1)
    #     webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    #     time.sleep(1)
    #     tprofile.click_state_biller()
    #     time.sleep(1)
    #     webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
    #     time.sleep(4)
    #     tprofile.enter_state_label("tax label")
    #     tprofile.enter_state_sgst("-5")
    #     tprofile.enter_state_cgst("-10")
    #     tprofile.enter_state_cess("-1")
    #
    #     tprofile.click_save_state()
    #     time.sleep(1)
    #
    #     text = driver.find_element(By.XPATH, "//div[@role='alert']").text
    #     popup = "sgst_ugst must not be less than 0.0"
    #     if text in popup:
    #         print(f"Valid Alert:> {popup}.")
    #     else:
    #         print(f"Invalid Alert:> {text}.")
    #
    #     webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    #     dashboard.page_scroll_to_top()
    #     tprofile.click_back()
    #     time.sleep(1)
    #     dashboard.click_account()
    #     time.sleep(2)
    #     dashboard.click_logout()


    # def test_017_tax(self):
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
    #     dashboard.click_tax_configuration()
    #     time.sleep(1)
    #     tprofile = AddTaxProfilePage(driver)
    #     tprofile.click_add_tax_profile()
    #     tprofile.enter_profile_name(fake_word)
    #     tprofile.click_save()
    #     time.sleep(2)
    #     tprofile.click_settings_icon()
    #     time.sleep(1)
    #     tprofile.click_manual_type()
    #     dashboard.page_scroll_to_bottom()
    #     tprofile.click_add_state_tax_config()
    #     time.sleep(1)
    #     tprofile.click_state_biller()
    #     time.sleep(1)
    #     webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    #     time.sleep(1)
    #     tprofile.click_state_biller()
    #     time.sleep(1)
    #     webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
    #     time.sleep(4)
    #     tprofile.enter_state_label("tax label")
    #     tprofile.enter_add_state_tax_rate("105")
    #     tprofile.click_save_state()
    #     time.sleep(1)
    #
    #     text = driver.find_element(By.XPATH, "//div[@role='alert']").text
    #     popup = "tax_rate must not be higher than 100.00"
    #     if text in popup:
    #         print(f"Valid Alert:> {popup}.")
    #     else:
    #         print(f"Invalid Alert:> {text}.")
    #
    #     webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    #     dashboard.page_scroll_to_top()
    #     tprofile.click_back()
    #     time.sleep(1)
    #     dashboard.click_account()
    #     time.sleep(2)
    #     dashboard.click_logout()


    # def test_018_tax(self):
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
    #     dashboard.click_tax_configuration()
    #     time.sleep(1)
    #     tprofile = AddTaxProfilePage(driver)
    #     tprofile.click_add_tax_profile()
    #     tprofile.enter_profile_name(fake_word)
    #     tprofile.click_save()
    #     time.sleep(2)
    #     tprofile.click_settings_icon()
    #     time.sleep(1)
    #     tprofile.click_manual_type()
    #     dashboard.page_scroll_to_bottom()
    #     tprofile.click_add_state_tax_config()
    #     time.sleep(1)
    #     tprofile.click_state_biller()
    #     time.sleep(1)
    #     webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    #     time.sleep(1)
    #     tprofile.click_state_biller()
    #     time.sleep(1)
    #     webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
    #     time.sleep(4)
    #     tprofile.enter_state_label("tax label")
    #     tprofile.enter_add_state_tax_rate("-5")
    #     tprofile.click_save_state()
    #     time.sleep(1)
    #
    #     text = driver.find_element(By.XPATH, "//div[@role='alert']").text
    #     popup = "tax_rate must not be less than 0.0"
    #     if text in popup:
    #         print(f"Valid Alert:> {popup}.")
    #     else:
    #         print(f"Invalid Alert:> {text}.")
    #
    #     webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    #     dashboard.page_scroll_to_top()
    #     tprofile.click_back()
    #     time.sleep(1)
    #     dashboard.click_account()
    #     time.sleep(2)
    #     dashboard.click_logout()


    # def test_019_tax(self):
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
    #     dashboard.click_tax_configuration()
    #     time.sleep(1)
    #     tprofile = AddTaxProfilePage(driver)
    #     tprofile.click_add_tax_profile()
    #     tprofile.enter_profile_name(fake_word)
    #     tprofile.click_save()
    #     time.sleep(2)
    #     tprofile.click_settings_icon()
    #     time.sleep(1)
    #     dashboard.page_scroll_to_bottom()
    #     tprofile.click_add_state_tax_config()
    #     time.sleep(1)
    #     tprofile.click_state_biller()
    #     time.sleep(1)
    #     webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    #     time.sleep(1)
    #     tprofile.click_state_biller()
    #     time.sleep(1)
    #     webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
    #     time.sleep(4)
    #     tprofile.enter_state_label("tax label")
    #     tprofile.enter_state_sgst("55")
    #     tprofile.enter_state_cgst("99")
    #     tprofile.enter_state_cess("75")
    #     tprofile.click_save_state()
    #     time.sleep(1)
    #
    #     text = driver.find_element(By.XPATH, "//div[@role='alert']").text
    #     popup = "Default tax profile must be configured, before configuring state wise tax config"
    #     if text in popup:
    #         print(f"Valid Alert:> {popup}.")
    #     else:
    #         print(f"Invalid Alert:> {text}.")
    #
    #     webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    #     dashboard.page_scroll_to_top()
    #     tprofile.click_back()
    #     time.sleep(1)
    #     dashboard.click_account()
    #     time.sleep(2)
    #     dashboard.click_logout()


    def test_020_tax(self):
        driver = self.driver
        driver.get(self.priyanshu_tenant)

        login = LoginPage(driver)
        # login.enter_tenant("priyanshu")
        # login.enter_continue()
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
        dashboard.page_scroll_to_bottom()
        tprofile.click_add_state_tax_config()
        time.sleep(1)
        tprofile.click_state_biller()
        time.sleep(1)
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        time.sleep(1)
        tprofile.click_state_biller()
        time.sleep(1)
        webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
        time.sleep(4)
        tprofile.enter_state_label("tax label")
        tprofile.enter_add_state_tax_rate("66")
        tprofile.click_save_state()
        time.sleep(1)

        text = driver.find_element(By.XPATH, "//div[@role='alert']").text
        popup = "Default tax profile must be configured, before configuring state wise tax config"
        if text in popup:
            print(f"Valid Alert:> {popup}.")
        else:
            print(f"Invalid Alert:> {text}.")

        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        dashboard.page_scroll_to_top()
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


