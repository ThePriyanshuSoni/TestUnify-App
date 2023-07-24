from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select



class CustCreate(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        actions = ActionChains(cls.driver)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_cust_create(self):
        self.driver.get("http://unifyng.inventum.co/login")
        self.driver.find_element(By.XPATH, "//input[@id='tenant']").send_keys("priyanshu")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Continue']").click()
        self.driver.find_element(By.XPATH, "//input[@id='username']").send_keys("priyanshu")
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("password")
        self.driver.find_element(By.XPATH, "//input[@id='kc-login']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//span[normalize-space()='CRM Management']").click()
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Customers']").click()
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Add New']").click()
        # Adding New Customer
        self.driver.find_element(By.XPATH, "//input[@id='crmCustomerId']").send_keys("TestKVM")
        self.driver.find_element(By.XPATH, "//input[@id='firstName']").send_keys("Test123")
        self.driver.find_element(By.XPATH, "//input[@id='lastName']").send_keys("testing")
        #self.driver.find_element(By.XPATH, "//div[@id='billerId']").click()
        time.sleep(5)
        #self.driver.find_element(By.XPATH, "//div[@id='billerId']").send_keys(Keys.ARROW_DOWN, Keys.ARROW_DOWN)
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//input[@id='tags']").click()
        self.driver.find_element(By.XPATH, "//input[@id='tags']").send_keys(Keys.ARROW_DOWN, Keys.ENTER)
        self.driver.find_element(By.XPATH, "//textarea[@id='notes']").send_keys("Test8ihg iudshiugdsuijb iusbdsiu fsd")
        self.driver.find_element(By.XPATH, "//input[@id='email']").send_keys("hello@test.com")
        self.driver.find_element(By.XPATH, "//input[@id='phoneNo']").send_keys("9191919191")
        self.driver.find_element(By.XPATH, "//input[@id='fullName']").send_keys("Priyanshu Soni")
        self.driver.find_element(By.XPATH, "//textarea[@id='addressLine']").send_keys("Address Test Line")
        self.driver.find_element(By.XPATH, "//input[@id='landmark']").send_keys("Near Inventum")
        self.driver.find_element(By.XPATH, "//input[@id='pincode']").send_keys("201305")
        self.driver.find_element(By.XPATH, "//input[@id='city']").send_keys("Noida")
        self.driver.find_element(By.XPATH, "//div[@id='country']").click()
        self.driver.find_element(By.XPATH, "//li[102]").click()
        self.driver.find_element(By.XPATH, "//div[@id='state']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//li[normalize-space()='Uttar Pradesh']").click()
        self.driver.find_element(By.XPATH, "//input[@id='6486f58f3dca617e7fcabaa5']").send_keys("PriyanshuSoni")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test Pass")


if __name__ == '__main__':
    unittest.main()