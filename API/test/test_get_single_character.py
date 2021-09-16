from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient, APITestCase

from API.models import CharacterModel


class TestGetSingleCharacter(APITestCase):
    client = APIClient()

    def setUp(self):
        get_user_model().objects.create(
            email="test@email.com",
            username="testMan",
            password="test12345"
        )
        self.user = get_user_model().objects.get(email="test@email.com")
        self.url = reverse('character_quote', kwargs={'pk': '5cd96e05de30eff6ebcce7e9'})

    def test_unauthorized_user_cannot_get_character_quote(self):
        res = self.client.get(self.url)
        self.assertEqual(res.status_code, 401)
    
    def test_authorized_user_can_get_character_quote(self):
        self.client.force_authenticate(user=self.user)
        res = self.client.get(self.url)
        self.assertEqual(res.status_code, 200)