from django.urls import reverse
from rest_framework import status

from core.tests import BaseApiTest
from posts.tests.factories import PostFactory


class PostListApiTests(BaseApiTest):
    count_posts = 20

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.url = reverse('posts:post_list')
        cls.posts = PostFactory.create_batch(cls.count_posts)

    def test_auth_credentials_are_necessary(self):
        self._test_auth_credentials(url=self.url, method='get')

    def test_post_list(self):
        token = self.get_token(email=self.email, password=self.password)
        res = self.make_authenticated_request(url=self.url, method='get', jwt_token=token)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
