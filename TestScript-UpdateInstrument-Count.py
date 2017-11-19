import unittest
import time
import django.utils.timezone

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Blog_UpdateInstrumentCount(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()




   def test_blog(self):
       driver = self.driver
       driver.maximize_window()
       driver.get("http://mavplay-music-fiesta.herokuapp.com/")
       assert "Logged In"

       # To select the product
       elem = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/a")
       elem.click()
       time.sleep(2)
       #aUpdate Count
       elem = driver.find_element_by_xpath("//select[@id='id_quantity']/option[@value='2']")
       elem.click()
       time.sleep(2)
       #Click on Add to Cart button
       elem = driver.find_element_by_xpath("/html/body/div[3]/div/form/input[3]")
       elem.click()
       time.sleep(2)
       #Update Count from inside the shopping cart
       elem = driver.find_element_by_xpath("//select[@id='id_quantity']/option[@value='4']")
       elem.click()
       time.sleep(2)
       # Click on Update
       elem = driver.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[1]/td[3]/form/input[2]")
       elem.click()
       time.sleep(2)


   def tearDown(self):
       self.driver.close()
