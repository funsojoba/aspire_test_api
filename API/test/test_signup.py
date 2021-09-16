from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class ModelTests(APITestCase):
    def setUp(self):
        self.signup_url = reverse('sign_up')

        self.no_username = {
            'email': 'email@email.com',
            'username': '',
            'password': 'testing321',
        }
        self.no_password = {
            'email': 'email@email.com',
            'username': 'testing321',
            'password': '',
        }

        return super().setUp()

    def test_create_user_successful(self):
        """Test creating new user with an email is successful"""
        email = 'test@testing.com'
        username = 'TestUser'
        password = 'testpasss321'
        user = get_user_model().objects.create_user(
            email=email, password=password, username=username
        )

        self.assertEqual(user.email, email)
        self.assertEqual(user.username, username)
        self.assertTrue(user.check_password(password))
    
    def test_user_without_username_cannot_creaate(self):
        self.client = APIClient()
        response = self.client.post(self.signup_url, self.no_username)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_without_password_cannot_register(self):
        self.client = APIClient()
        response = self.client.post(self.signup_url, self.no_password)
        self.assertEqual(response.status_code, 400)