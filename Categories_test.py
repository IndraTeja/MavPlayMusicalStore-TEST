import unittest
import time
from selenium import webdriver


class CategoriesTest(unittest.TestCase):

    def setUp(self):
       self.driver = webdriver.Chrome()

    def test_blog(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://mavplay-music-fiesta.herokuapp.com/")
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/div[3]/div[1]/ul/li[2]/a")
        elem.click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div[3]/div[1]/ul/li[3]/a")
        elem.click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div[3]/div[1]/ul/li[4]/a")
        elem.click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div[3]/div[1]/ul/li[5]/a")
        elem.click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div[3]/div[1]/ul/li[6]/a")
        elem.click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div[3]/div[1]/ul/li[1]/a")
        elem.click()
        time.sleep(2)

        def tearDown(self):
            self.driver.close()


if __name__ == "__main__":
    unittest.main()
