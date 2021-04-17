from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.utils import timezone

from users.services import get_user_last_activity_data
from users.models import User
from users.tests.factories import UserFactory, UserLastActivityFactory


class GetUserLastActivityDataServiceTests(TestCase):

    def setUp(self) -> None:
        self.user = UserFactory(last_login=timezone.now())
        self.last_activity = UserLastActivityFactory(user=self.user)

    def test_get_user_last_activity_data_service(self):
        data = get_user_last_activity_data(user=self.user, last_activity=self.last_activity)
        self.assertEqual(data['last_login_date'], self.user.last_login)
        self.assertEqual(data['last_request_date'], self.last_activity.created_at)
        self.assertEqual(data['last_request_url'], self.last_activity.url)

