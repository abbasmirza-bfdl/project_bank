from django.test import TestCase

# Create your tests here.
from django.test import TestCase

class StatusCodes(TestCase):
    def test_home_page(self):
        response=self.client.get('/')
        self.assertEqual(response.status_code,200,'Could not connect to launch page. Check connection!')

    def test_user_reg_page(self):
        response=self.client.get('/selfregister/')
        self.assertEqual(response.status_code,200,'Could not connect to user register page. Check connection!')

    def test_admin_login_page(self):
        response=self.client.get('/bankadmin/login/')
        self.assertEqual(response.status_code,200,'Could not connect to admin login page. Check connection!')