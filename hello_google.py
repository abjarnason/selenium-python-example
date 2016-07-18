from selenium import webdriver
import unittest
import sys

class ExampleTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor="http://192.168.1.52:4444/wd/hub",
            desired_capabilities={
            "browserName": "internet explorer",
            "platform": "WINDOWS",
            "version": 8,
        })

    def test_two_is_two(self):
        self.assertEqual(2,2)

    def test_hello_google(self):
        self.driver.get("http://www.google.com")
        self.assertEqual(self.driver.title, "Google")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

