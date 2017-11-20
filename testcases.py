import unittest
import time
from selenium import webdriver


class MavPlay(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_blog(self):

         driver = self.driver
         driver.maximize_window()

         driver = self.driver
         driver.maximize_window()
         driver.get("http://mavplay-music-fiesta.herokuapp.com/")# shows up the product page
         time.sleep(2)
         elem = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/a").click()#adds the first product from the page
         time.sleep(2)
         elem = driver.find_element_by_xpath("/html/body/div[3]/div/form/input[3]").click()#shows the product in your shopping cart
         time.sleep(2)
         elem = driver.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[1]/td[4]/a").click()#removes product from the cart
         time.sleep(2)
         elem = driver.find_element_by_xpath("/html/body/div[3]/p/a[1]").click()#prompts for continue shopping
         time.sleep(3)



    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
