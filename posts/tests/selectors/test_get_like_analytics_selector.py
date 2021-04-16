from datetime import timedelta
from django.test import TestCase
from django.utils.datetime_safe import date

from posts.tests.factories import PostFactory, LikeFactory
from posts.selectors import get_like_analytics
from posts.models import Post, Like
from users.tests.factories import UserFactory


class GetLikeAnalyticsSelectorTest(TestCase):
    date_from = date(2021, 1, 1)
    date_to = date(2021, 1, 5)

    def setUp(self) -> None:
        start_date = self.date_from
        end_date = self.date_to
        delta = timedelta(days=1)

        while start_date <= end_date:
            res = LikeFactory.create_batch(5, kind=True)
            res += LikeFactory.create_batch(2, kind=False)
            Like.objects.filter(id__in=[like.id for like in res]).update(created_at=start_date)
            start_date += delta

    def test_get_like_analytics_selector(self):
        analytics_list = list(get_like_analytics(date_from=self.date_from, date_to=self.date_to))
        self.assertEqual(len(analytics_list), 5)
        for day in analytics_list:
            self.assertEqual(day['likes'], 5)
            self.assertEqual(day['dislikes'], 2)






