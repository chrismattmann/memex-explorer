"""
Testing project creation.
"""

#  IMPORTS
# =========

from test_skeleton import TestSkeleton


class RegisterProjectTest(TestSkeleton):

    #  SETUP & TEARDOWN
    # ==================
    # Not required to unit test projects (no side effects)


    #  UNIT TESTS
    # ============

    def test_page_exists(self):
        """Test if `/add_project` endpoint exists."""
        rv = self.test_app.get('/add_project')
        self.assertEqual(rv.status_code, 200)

    def test_no_data(self):
        """"Send a POST request with no data."""

        data = {}

        rv = self.test_app.post('/add_project', data=data, follow_redirects=True)
        self.assertIn("This field is required.", rv.data)

    def test_partial_data(self):
        """Send a POST request with partial data."""

        data = {"description": "test test"}

        rv = self.test_app.post('/add_project', data=data, follow_redirects=True)
        self.assertIn("This field is required.", rv.data)

    def test_register_project(self):
        """Register a valid project."""

        data = {"name": "cats",
                "description": "Cats are cute!",
                "icon": "fa-arrows"}

        rv = self.test_app.post('/add_project', data=data, follow_redirects=True)
        self.assertIn("Project &#39;cats&#39; was successfully registered", rv.data)


    def test_duplicate_project(self):
        """Register a duplicate project."""

        data = {"name": "cats",
                "description": "Cats are cute!",
                "icon": "fa-arrows"}

        rv = self.test_app.post('/add_project', data=data, follow_redirects=True)
        self.assertIn("Project &#39;cats&#39; was successfully registered", rv.data)

        rv = self.test_app.post('/add_project', data=data, follow_redirects=True)
        self.assertIn("Project &#39;cats&#39; already exists", rv.data)
