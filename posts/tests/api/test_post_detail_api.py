from rest_framework import status
from django.urls import reverse

from core.tests import BaseApiTest
from posts.tests.factories import PostFactory


class PostDetailApiTests(BaseApiTest):

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.post = PostFactory()
        cls.url = reverse('posts:post_detail', args=[cls.post.id])

    def test_auth_credentials_are_necessary(self):
        self._test_auth_credentials(url=self.url, method='get')

    def test_post_detail(self):
        token = self.get_token(email=self.email, password=self.password)
        res = self.make_authenticated_request(url=self.url, method='get', jwt_token=token)
        self.assertEqual(res.status_code, status.HTTP_200_OK)


