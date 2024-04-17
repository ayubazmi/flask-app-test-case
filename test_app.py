import unittest
from app import app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        # Create a test client
        self.app = app.test_client()
        self.app.testing = True

    def test_home_route(self):
        # Send a GET request to the home route
        response = self.app.get('/')
        # Check if the status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Check if the response contains the expected content
        self.assertTrue(b'<title>My Flask App</title>' in response.data)
        self.assertTrue(b'<h1>Hello, World!</h1>' in response.data)
        self.assertTrue(b'<p>Welcome to my Flask app.</p>' in response.data)

    def test_about_route(self):
        # Send a GET request to the about route
        response = self.app.get('/about')
        # Check if the status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Check if the response contains the expected content
        self.assertEqual(response.data.decode('utf-8'), 'This is the About page.')

if __name__ == '__main__':
    unittest.main()
