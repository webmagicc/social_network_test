from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

from users.services import user_create
from users.models import User


class UserCreateTests(TestCase):
    email = 'user@example.com'
    password = 'Ghbdtnvbh'
    first_name = 'John'
    last_name = 'Doe'

    def test_user_create_full_data(self):
        user = user_create(
            email=self.email,
            password=self.password,
            first_name=self.first_name,
            last_name=self.last_name
        )
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(user.email, self.email)
        self.assertEqual(user.first_name, self.first_name)
        self.assertEqual(user.last_name, self.last_name)
        self.assertTrue(user.check_password(self.password))

    def test_user_create_with_same_email(self):
        user_create(
            email=self.email,
            password=self.password
        )
        with self.assertRaises(IntegrityError):
            user_create(
                email=self.email,
                password=self.password
            )

    def test_user_create_with_weak_password(self):
        with self.assertRaises(ValidationError):
            user_create(
                email=self.email,
                password='12345'
            )
        with self.assertRaises(ValidationError):
            user_create(
                email=self.email,
                password='123455678'
            )


