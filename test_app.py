import unittest
from app import app, users

class FlaskAuthTestCase(unittest.TestCase):

    def setUp(self):
        # Setup test client
        self.app = app.test_client()
        self.app.testing = True
        users.clear()  # Clear users before each test

    def test_signup_success(self):
        response = self.app.post('/login', data={
            'username': 'testuser',
            'password': 'testpass',
            'action': 'Signup'
        })
        self.assertIn(b'Signup successful for user: testuser', response.data)

    def test_signup_existing_user(self):
        users['testuser'] = 'testpass'
        response = self.app.post('/login', data={
            'username': 'testuser',
            'password': 'newpass',
            'action': 'Signup'
        })
        self.assertIn(b"Username 'testuser' already exists", response.data)

    def test_login_success(self):
        users['testuser'] = 'testpass'
        response = self.app.post('/login', data={
            'username': 'testuser',
            'password': 'testpass',
            'action': 'Login'
        })
        self.assertIn(b'Welcome back, testuser!', response.data)

    def test_login_wrong_password(self):
        users['testuser'] = 'correctpass'
        response = self.app.post('/login', data={
            'username': 'testuser',
            'password': 'wrongpass',
            'action': 'Login'
        })
        self.assertIn(b'Incorrect password for user: testuser', response.data)

    def test_login_nonexistent_user(self):
        response = self.app.post('/login', data={
            'username': 'nouser',
            'password': 'pass',
            'action': 'Login'
        })
        self.assertIn(b"Username 'nouser' not found", response.data)

    def test_invalid_action(self):
        response = self.app.post('/login', data={
            'username': 'anyuser',
            'password': 'anypass',
            'action': 'Unknown'
        })
        self.assertIn(b'Unknown action.', response.data)

if __nam__ == '__main__':
    unittest.main()