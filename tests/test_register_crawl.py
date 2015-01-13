"""
Testing crawl creation.
"""

from test_skeleton import TestSkeleton

from app.models import Project

class RegisterCrawlTest(TestSkeleton):

    def setUp(self):
        super(RegisterCrawlTest, self).setUp()

        project = Project(slug="project",
                          name="project",
                          description="Description.",
                          icon="fa-arrows")
        self.test_db.session.add(project)
        self.test_db.session.commit()

    def test_page_exists(self):
        """Test if `project/add_crawl` endpoint exists."""
        rv = self.test_app.get('project/add_crawl')
        self.assertEqual(rv.status_code, 200)

    def test_post_no_data(self):
        """"Send a POST request with no data."""

        data = {}

        rv = self.test_app.post('project/add_crawl', data=data, follow_redirects=True)
        self.assertEqual(rv.status_code, 200)
        self.assertIn("This field is required.", rv.data)

    def test_post_partial_data(self):
        """Send a POST request with partial data."""

        rv = self.test_app.get('/')
        data = {"description": "test test"}

        rv = self.test_app.post('/project/add_crawl', data=data, follow_redirects=True)
        self.assertEqual(rv.status_code, 200)
        self.assertIn("This field is required.", rv.data)

    def test_register_nutch_crawl(self):
        """Register a Nutch crawl."""

        from StringIO import StringIO

        data = {"name": "UNIQUETITLE",
                "description": "DESCRIPTION",
                "crawler": "nutch",
                # Emulate file upload with StringIO
                "seeds_list": (StringIO(
                    "https://www.youtube.com/watch?v=dQw4w9WgXcQ"), 'seeds.txt')}

        rv = self.test_app.post('/project/add_crawl', buffered=True,
            content_type='multipart/form-data', data=data, follow_redirects=True)
        self.assertEqual(rv.status_code, 200)
        self.assertIn("UNIQUETITLE", rv.data)

    # def test_duplicate_insert(self):
    #     """test error handling of duplicate data"""

    #     rv = self.test_app.get('/')

    #     data = {"description": "DESCRIPTION", "name": "UNIQUETITLE"}

    #     # Posting bad data should still generate a 200 OK
    #     rv = self.test_app.post('/project/add_crawl', data=data)
    #     self.assertEqual(rv.status_code, 200)

    #     rv = self.test_app.post('/project/add_crawl', data=data)
    #     self.assertEqual(rv.status_code, 200)
    #     self.assertIn("has already been registered-please provide another name.", rv.data)
