import unittest

from tests.test_front_page import ServerUpTest
from tests.test_register_project import RegisterProjectTest
from tests.test_register_crawl import RegisterCrawlTest


def suite():
    suite = unittest.TestSuite()

    suite.addTest(unittest.makeSuite(ServerUpTest))
    suite.addTest(unittest.makeSuite(RegisterProjectTest))
    suite.addTest(unittest.makeSuite(RegisterCrawlTest))

    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)
