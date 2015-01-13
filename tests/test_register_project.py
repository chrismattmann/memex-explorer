"""
Testing project creation.
"""

from test_skeleton import TestSkeleton

class RegisterProjectTest(TestSkeleton):

    def test_page(self):
        """Test if `/add_project` endpoint exists."""
        response = self.test_app.get('/add_project')
        assert response.status_code == 200

    def test_no_data(self):
        """test error handling of no data being supplied during submit"""

        data = {}

        # Bad Post is still a 200 OK
        rv = self.test_app.post('/add_project', data=data, follow_redirects=True)
        self.assertEqual(rv.status_code, 200)
        self.assertIn("This field is required.", rv.data)

    def test_partial_data(self):
        """test error handling of partial data in form"""

        data = {"description": "test test"}

        # Posting bad data should still generate a 200 OK
        rv = self.test_app.post('/add_project', data=data, follow_redirects=True)
        self.assertEqual(rv.status_code, 200)
        self.assertIn("This field is required.", rv.data)

    def test_insert_data(self):
        """test proper insertion"""

        data = {"name": "UNIQUETITLE",
                "description": "DESCRIPTION",
                "icon": "fa-arrows"}

        rv = self.test_app.post('/add_project', data=data, follow_redirects=True)

        self.assertEqual(rv.status_code, 200)
        self.assertIn("Project &#39;UNIQUETITLE&#39; was successfully registered", rv.data)


    def test_duplicate_insert(self):
        """test error handling of duplicate data"""

        data = {"name": "UNIQUETITLE",
                "description": "DESCRIPTION",
                "icon": "fa-arrows"}

        rv = self.test_app.post('/add_project', data=data, follow_redirects=True)
        
        self.assertEqual(rv.status_code, 200)
        self.assertIn("Project &#39;UNIQUETITLE&#39; was successfully registered", rv.data)


        # POST same data again
        rv = self.test_app.post('/add_project', data=data, follow_redirects=True)
        self.assertEqual(rv.status_code, 200)
        self.assertIn("Project &#39;UNIQUETITLE&#39; already exists", rv.data)
