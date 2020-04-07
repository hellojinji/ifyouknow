from selenium import webdriver
import unittest

from selenium.webdriver.common.keys import Keys
import time


class NewVisitorTest(unittest.TestCase):  #1

    def setUp(self):  #2
        self.browser = webdriver.Firefox(log_path=r"D:/geckodriver.log")
        #self.browser.implicitly_wait(100)
		
    def tearDown(self):  #3
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):  #4
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)  #5
        header_text=self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
		
        inputbox=self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a to-do item')
		
        inputbox.send_keys('buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        table=self.browser.find_element_by_id('id_list_table')
        rows=table.find_element_by_tag_name('tr')
        self.assertTrue(any(row.text=='1: Buy peacock feather' for row in rows))
        self.fail('Finish the test!')  #6


      

if __name__ == '__main__':  #7
    unittest.main(warnings='ignore')  #8888888888
