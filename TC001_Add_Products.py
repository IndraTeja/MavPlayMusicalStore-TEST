#Author : Indra Teja Chintakayala
#Assignment 3
#ISQA4900

#modules
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv

#
class admin_add_product(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_blog(self):
        user = "mavplay"
        pwd = "mavplay2017"
        driver = self.driver
        driver.maximize_window()
        driver.get("https://mavplay-music-fiesta.herokuapp.com/")
        time.sleep(3)
        driver.get("https://mavplay-music-fiesta.herokuapp.com//admin/")
        time.sleep(3)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        time.sleep(2)
        assert "Logged In"
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[3]/table/tbody/tr[2]/th/a")
        elem.click()
        time.sleep(2)

        #Delete all the products
        driver.find_element_by_id("action-toggle").click()


        with open('products.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/ul/li/a")
                elem.click()
                time.sleep(2)
                dropdown = driver.find_element_by_xpath(line[0])
                dropdown.click()
                elem = driver.find_element_by_id("id_name")
                elem.send_keys(line[1])
                time.sleep(2)
                elem = driver.find_element_by_id("id_image")
                elem.send_keys(line[5])
                time.sleep(2)
                elemt = driver.find_element_by_id("id_description")
                elemt.send_keys(line[2])
                time.sleep(2)
                elem = driver.find_element_by_id("id_price")
                elem.send_keys(line[3])
                time.sleep(2)
                elem = driver.find_element_by_id("id_stock")
                elem.send_keys(line[4])
                time.sleep(2)
                elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/form/div/div/input[1]")
                elem.click()


    def tearDown(self):
                self.driver.close()

if __name__ == "__main__":
    unittest.main()

