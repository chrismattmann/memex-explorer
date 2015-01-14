"""
Testing proper rendering of the front page.
"""

from test_skeleton import TestSkeleton

class ServerUpTest(TestSkeleton):

    def test_page_exists(self):
        """Test if root page exists."""
        rv = self.test_app.get('/')
        self.assertEqual(rv.status_code, 200)

    def test_title(self):
        """Test title of root page."""
        rv = self.test_app.get('/')
        self.assertIn('MEMEX EXPLORER', rv.data)
