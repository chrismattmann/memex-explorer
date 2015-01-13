# import mock
# from nose.tools import *
# import re
# import requests
# from bs4 import BeautifulSoup
# from tests.fixtures import mock_links, mock_urls, mock_forms

import unittest

from robobrowser.browser import RoboBrowser
from robobrowser import exceptions

from test_skeleton import TestSkeleton


class RegisterCrawlTest(TestSkeleton):

    def setUp(self):
        super(RegisterCrawlTest, self).setUp()

class TestHeaders(unittest.TestCase):

    HOME_PAGE = "http://localhost:5000/"

    @classmethod
    def setUpClass(cls):

    @mock_links
    def test_user_agent(self):
        browser = RoboBrowser(user_agent='MEMEX_TESTER')
        browser.open(HOME_PAGE)
        assert_true('User-Agent' in browser.session.headers)
        assert_equal(
            browser.session.headers['User-Agent'], 'MEMEX_TESTER'
        )

    def test_default_headers(self):
        browser = RoboBrowser()
        assert_equal(browser.session.headers, requests.Session().headers)


    @classmethod
    def tearDownClass(cls):
