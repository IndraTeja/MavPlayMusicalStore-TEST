import unittest
import time
import django.utils.timezone

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Blog_MavPlay_AddToCart(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()




   def mavPlay_addToCart(self):
       driver = self.driver
       driver.maximize_window()
       driver.get("http://mavplay-music-fiesta.herokuapp.com/")
       assert "Logged In"

       # To select the product
       elem = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/a")
       elem.click()
       time.sleep(2)
       #add to Cart
       elem = driver.find_element_by_xpath("/html/body/div[3]/div/form/input[3]")
       elem.click()
       time.sleep(2)
       #Continue Shopping
       elem = driver.find_element_by_xpath("/html/body/div[3]/p/a[1]")
       elem.click()
       time.sleep(2)
       #Select Product
       elem = driver.find_element_by_xpath("//html/body/div[3]/div[2]/div[5]/a")
       elem.click()
       time.sleep(2)
       # add to Cart
       elem = driver.find_element_by_xpath("/html/body/div[3]/div/form/input[3]")
       elem.click()
       time.sleep(2)





   def tearDown(self):
       self.driver.close()
