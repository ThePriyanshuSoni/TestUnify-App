from selenium import webdriver
import time
import unittest

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class custCreate(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_customer_create(self):
        self.driver.get("http://unifyng.inventum.co/login")
        self.driver.find_element(By.XPATH, "//input[@id='tenant']").send_keys("priyanshu")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Continue']").click()
        self.driver.find_element(By.XPATH, "//input[@id='username']").send_keys("priyanshu")
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("password")
        self.driver.find_element(By.XPATH, "//input[@id='kc-login']").click()
        time.sleep(3)
        self. driver.find_element(By.XPATH, "//span[normalize-space()='CRM Management']").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test Pass")
