from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Maria has heard about a cool online to-do list app.
        # she goes to the website to see its homepage
        self.browser.get('http://localhost:8000')

        # she notices the page title and header mention to-do lists
        self.assertIn('To-do', self.browser.title)
        self.fail('Finish the test!')

        # she is invited to enter a to-do item straight away

        # she types "buy bacalhau for dinner" into a text box

        # when she hits Enter, the page updates and now the page displays
        # "1: Buy bacalhau for dinner" as an item in a to-do list.

        # There is still a text box inviting her to add another item,. She enters
        # "Clear the rubbish outside"

        # The page updates again and now both items show on her list.

        # Maria wonders whether the site will remember her list. Then she sees that the site has
        # generated a unique URL for here -- there is some explanatory text to that effect

        # she visits that url an her to-do list is intact

        # Maria goes to bed.


if __name__ == '__main__':
    unittest.main(warnings='ignore')