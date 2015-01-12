"""
Testing proper rendering of the front page.
"""

from test_skeleton import TestSkeleton

class ServerUpTest(TestSkeleton):

    def test_get_test(self):
        """Does hitting the /test endpoint return the proper HTTP code?"""
        response = self.app.get('/')
        assert response.status_code == 200

    def test_title(self):
        """test title of root page"""
        rv = self.app.get('/')
        self.assertIn('MEMEX EXPLORER', rv.data)
