
from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker

from intraApp.models import User


class TestSetUp(APITestCase):

    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.list_user_url = reverse('list-user')
        # self.detail_user_url = reverse('detail-user', id=1)
        self.obtain_token_url = reverse('token_obtain_pair')
        self.refresh_token_url = reverse('token_refresh')
        self.verify_token_url = reverse('token_verify')
        self.fake = Faker()

        self.user_data = {
            'email': self.fake.email(),
            'password': self.fake.password(),
        }

        return super().setUp()

    def tearDown(self):
        return super().tearDown()