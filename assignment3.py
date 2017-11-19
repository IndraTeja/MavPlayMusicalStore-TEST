import unittest
import time
from selenium import webdriver


class Blog_ATS(unittest.TestCase):

   def setUp(self):
       #set the chrome webdriver
       self.driver = webdriver.Chrome()

   def test_blog(self):

       driver = self.driver
       driver.maximize_window()
       #go to the website homepage
       driver.get("http://mavplay-music-fiesta.herokuapp.com")#goes to main page
       time.sleep(3)
       #find element by xpath, adds item to the cart
       elem = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/a").click()
       time.sleep(3)
       #click the add cart button
       elem = driver.find_element_by_xpath("/html/body/div[3]/div/form/input[3]").click()
       time.sleep(3)

       #clicks the checkout button
       elem = driver.find_element_by_xpath("/html/body/div[3]/p/a[2]").click()
       time.sleep(3)
       # find the element by ID
       elem = driver.find_element_by_id("id_first_name")
       # type in the value
       elem.send_keys("Suvid")
       time.sleep(2)
       elem = driver.find_element_by_id("id_last_name")
       elem.send_keys("Bhatta")
       time.sleep(2)
       elem = driver.find_element_by_id("id_email")
       elem.send_keys("suvb@gmail.com")
       time.sleep(2)
       elem = driver.find_element_by_id("id_address")
       elem.send_keys("174 R st")
       time.sleep(2)
       elem = driver.find_element_by_id("id_postal_code")
       elem.send_keys("68125")
       time.sleep(2)
       elem = driver.find_element_by_id("id_city")
       elem.send_keys("Omaha")
       time.sleep(2)

       #clicks place order button
       elem = driver.find_element_by_xpath("/html/body/div[3]/form/p[7]/input").click()
       time.sleep(2)

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()




