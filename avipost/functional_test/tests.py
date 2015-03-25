from selenium import webdriver
from django.test import LiveServerTestCase

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        #pass
        self.browser.quit()

    def test_home_page(self):
        self.browser.get(self.live_server_url)
        self.assertIn('AviPost', self.browser.title)

