from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.by import By


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(15)
        cls.driver.maximize_window()

    def test_login_valid(self):
        self.driver.get("http://unifyng.inventum.co/login")
        # self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        # self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        # self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test Done")