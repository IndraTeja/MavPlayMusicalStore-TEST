import unittest
import time
from selenium import webdriver


class HomeTest(unittest.TestCase):

    def setUp(self):
       self.driver = webdriver.Chrome()

    def test_blog(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://mavplay-music-fiesta.herokuapp.com/")
        time.sleep(5)

        def tearDown(self):
            self.driver.close()


if __name__ == "__main__":
    unittest.main()
