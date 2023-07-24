from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(15)
        cls.driver.maximize_window()

    def test_login_valid(self):
        self.driver.get("http://unifyng.inventum.co/login")
        self.driver.find_element(By.XPATH, "//input[@id='tenant']").send_keys("priyanshu")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Continue']").click()
        self.driver.find_element(By.XPATH, "//input[@id='username']").send_keys("priyanshu")
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("password")
        self.driver.find_element(By.XPATH, "//input[@id='kc-login']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//span[normalize-space()='CRM Management']").click()
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Customers']").click()
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Add New']").click()
        # Adding New Customer
        self.driver.find_element(By.XPATH, "//input[@id='crmCustomerId']").send_keys("TestKVM")
        self.driver.find_element(By.XPATH, "//input[@id='firstName']").send_keys("Test123")
        self.driver.find_element(By.XPATH, "//input[@id='lastName']").send_keys("testing")
        self.driver.find_element(By.XPATH, "//input[@id='tags']").click()
        self.driver.find_element(By.XPATH, "//input[@id='tags']").send_keys(Keys.ARROW_DOWN, Keys.ENTER)
        self.driver.find_element(By.XPATH, "//textarea[@id='notes']").send_keys("Test8ihg iudshiugdsuijb iusbdsiu fsd")
        self.driver.find_element(By.XPATH, "//div[@id='services']").click()
        self.driver.find_element(By.XPATH, "//li[@role='option']").click()
        self.driver.find_element(By.XPATH, "//input[@id='device_id']").send_keys("Testing")
        self.driver.find_element(By.XPATH, "//div[@id='net_id_type']").click()
        self.driver.find_element(By.XPATH, "//li[normalize-space()='MAC-Address']").click()
        self.driver.find_element(By.XPATH, "//input[@id='username']").send_keys("nbdkh34Cd46")
        self.driver.find_element(By.XPATH, "//input[@id='email']").send_keys("hello@test.com")
        self.driver.find_element(By.XPATH, "//input[@id='phoneNo']").send_keys("9191919191")
        self.driver.find_element(By.XPATH, "//input[@id='crmPolicyMapDto']").click()
        self.driver.find_element(By.XPATH, "//input[@id='crmPolicyMapDto']").send_keys(Keys.ARROW_DOWN, Keys.ENTER)
        self.driver.find_element(By.XPATH, "//input[@id='fullName']").send_keys("Priyanshu Soni")
        self.driver.find_element(By.XPATH, "//textarea[@id='addressLine']").send_keys("Address Test Line")
        self.driver.find_element(By.XPATH, "//input[@id='landmark']").send_keys("Near Inventum")
        self.driver.find_element(By.XPATH, "//input[@id='pincode']").send_keys("201305")
        self.driver.find_element(By.XPATH, "//input[@id='city']").send_keys("Noida")
        self.driver.find_element(By.XPATH, "//input[@id='state']").send_keys("UP")
        self.driver.find_element(By.XPATH, "//input[@id='country']").send_keys("India")
        self.driver.find_element(By.XPATH, "//input[@name='defaultAddress']").click()
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test Done")
