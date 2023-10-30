import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.headless = True
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        print("Done")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
