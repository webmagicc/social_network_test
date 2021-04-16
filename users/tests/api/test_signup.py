from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from users.models import User


class SignupTests(APITestCase):
    email = 'user@example.com'
    password = 'Ghbdtnvbh'
    first_name = 'John'
    last_name = 'Doe'

    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('users:signup')

    def test_signup_full_data(self):
        data = dict(
            email=self.email, password=self.password, password_repeat=self.password, first_name=self.first_name,
            last_name=self.last_name
        )
        res = self.client.post(self.url, data=data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED, res.json())
        user = User.objects.get(email=self.email)
        self.assertIsNotNone(user)
        self.assertEqual(user.first_name, self.first_name)
        self.assertEqual(user.last_name, self.last_name)
        self.assertTrue(user.check_password(self.password))

    def test_signup_with_email_password(self):
        data = dict(
            email=self.email, password=self.password, password_repeat=self.password
        )
        res = self.client.post(self.url, data=data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED, res.json())
        user = User.objects.get(email=self.email)
        self.assertIsNotNone(user)

    def test_signup_with_wrong_password_repeat(self):
        data = dict(
            email=self.email, password=self.password, password_repeat=self.password + '3'
        )
        res = self.client.post(self.url, data=data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST, res.json())
        user = User.objects.filter(email=self.email).first()
        self.assertIsNone(user)

