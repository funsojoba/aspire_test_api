from django.http import response
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from django.urls import reverse


class TestFetchAllCharacters(APITestCase):
    client = APIClient()

    def setUp(self):
        get_user_model().objects.create(
            email="ajibolagureje@gmail.com", password='123456'
        )
        self.user = get_user_model().objects.get(email='ajibolagureje@gmail.com')
        self.url = reverse('all_characters')

    def test_annonimous_user_cannot_get_characters(self):
        res = self.client.get(self.url)
        self.assertEqual(res.status_code, 401)
    
    def test_authenticated_user_can_get_characters(self):
        self.client.force_authenticate(user=self.user)
        res = self.client.get(self.url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
