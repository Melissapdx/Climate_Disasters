from unittest import TestCase
from app import app


class ClimateTests(TestCase):
    """Tests routes for Climate Disasters site"""

    def setUp(self):
        """Basic test setup"""
        self.client = app.test_client()
        app.config['TESTING'] = True

    def tearDown(self):
        pass

    def test_root_route(self):
        """Test root"""
        result = self.client.get('/')
        self.assertEqual(result.status_code, 200)

    def test_endpoints(self):
        """Test endpoints"""
        result = self.client.get('/api/v1/')
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.json, [{'disasters': '/api/v1/disasters'},
            {'disasters_by_type': '/api/v1/disasters/type/<string:type>'},
            {'disasters_by_year': '/api/v1/disasters/year/<string:year>'},
            {'disasters_by_year_and_type': '/api/v1/disasters/yeartype/<string:year>/<string:type>'}])

    def test_by_type(self):
        result = self.client.get('/api/v1/disasters/type/Human Cause')
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.json, {'NY': 1, 'OK': 1, 'FL': 4})

    def test_by_year(self):
        result = self.client.get('/api/v1/disasters/year/1960')
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.json, {'AR': 1, 'HI': 2, 'OK': 2, 'MO': 1, 'SD': 1, 'NE': 1, 'TX': 1, 'FL': 2, 'NC': 1, 'ID': 1})

    def test_by_year_and_type(self):
        result = self.client.get('/api/v1/disasters/yeartype/1980/Volcano')
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.json, {'WA': 39, 'ID': 8})

if __name__ == "__main__":
    import unittest
    unittest.main()
