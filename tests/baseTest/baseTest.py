import unittest
from selenium import webdriver

class BaseTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)


    def tearDown(self) -> None:
        self.driver.close()
