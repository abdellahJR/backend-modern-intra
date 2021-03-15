
from rest_framework import status
from rest_framework.test import APITestCase
from intraApp.models import Company, CustomUser



from rest_framework.test import RequestsClient



class CustomUserTests(APITestCase):
    def test_create_user(self):
        """
        Ensure we can create a new user object.
        """
        data = {
            "email": "test@test.com",
            "first_name": "test",
            "last_name": "testing",
            "user_type": "client",
            "secondaryEmails": []
        }
        response = self.client.post('http://localhost:8000/api/users/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(CustomUser.objects.get().email, 'test@test.com')
        # response = self.client.get('http://localhost:8000/api/users/1')
        # self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user_list(self):
        response = self.client.get('http://localhost:8000/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    # def test_get_user_detail(self):
    #     response = self.client.get('http://localhost:8000/api/users/1')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

