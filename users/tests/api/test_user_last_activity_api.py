from django.urls import reverse
from rest_framework import status

from core.tests import BaseApiTest


class UserLastActivityApiTests(BaseApiTest):

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.url = reverse('users:last_activity')

    def setUp(self) -> None:
        token = self.get_token(email=self.email, password=self.password)
        self.make_authenticated_request(url=self.url, method='get', jwt_token=token)

    def test_auth_credentials_are_necessary(self):
        self._test_auth_credentials(url=self.url, method='get')

    def test_last_activity(self):
        token = self.get_token(email=self.email, password=self.password)
        res = self.make_authenticated_request(url=self.url, method='get', jwt_token=token)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        json_data = res.json()
        self.assertIn('last_request_url', json_data)
        self.assertIn('last_request_date', json_data)
        self.assertIn('last_login_date', json_data)
        self.assertIn(self.url, json_data['last_request_url'])
