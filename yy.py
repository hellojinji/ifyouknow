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

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text  #1
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')  #1
      

        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')  #2

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list table
        inputbox.send_keys(Keys.ENTER)  #3
        time.sleep(1)  #4

        table = self.browser.find_element_by_id('id_list_table') #1
        rows = table.find_elements_by_tag_name('tr') 
        self.assertIn('1:Buy peacock feathers',[row.text for row in rows])
        self.assertIn('2:Use peacock feathers to make a fly',
        [row.text for row in rows])
        

        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very
        # methodical)
        self.fail('Finish the test!')


      

if __name__ == '__main__':  #7
    unittest.main(warnings='ignore')  #8888888888
