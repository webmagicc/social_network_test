from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.response import Response

from users.tests.factories import UserFactory


class BaseApiTest(APITestCase):
    email = 'user@example.com'
    password = 'Ghbdtnvbh'
    first_name = 'John'
    last_name = 'Doe'

    @staticmethod
    def create_user(*, email, password, first_name='', last_name='', is_active=True):
        user = UserFactory(email=email, first_name=first_name, last_name=last_name, is_active=is_active)
        user.set_password(password)
        user.save()
        return user

    @classmethod
    def setUpTestData(cls):
        cls.user = BaseApiTest.create_user(
            email=cls.email, password=cls.password, first_name=cls.first_name, last_name=cls.last_name
        )

    def get_token(self, *, email, password):
        url = reverse('token_obtain_pair')
        res = self.client.post(url, {'email': email, 'password': password}, format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in res.data)
        token = res.data['access']
        return token

    def verify_token(self, token: str):
        verification_url = reverse('api-jwt-verify')
        res = self.client.post(verification_url, {'token': token}, format='json')
        if res.status_code == status.HTTP_200_OK:
            return True
        return False

    @classmethod
    def make_authenticated_request(cls, *, url: str, method: str, jwt_token: str, **kwargs) -> Response:
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + jwt_token)
        client_method = getattr(client, method)
        if kwargs:
            res = client_method(url, data=kwargs)
        else:
            res = client_method(url)
        return res

    def _test_auth_credentials(self, url, method, data=None):
        resp = getattr(self.client, method)(url, data=data)
        self.assertEqual(resp.status_code, 401)
        self.assertEqual(resp.json(), {'detail': 'Authentication credentials were not provided.'})
