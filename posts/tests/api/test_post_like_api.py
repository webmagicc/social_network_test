from rest_framework import status
from django.urls import reverse

from core.tests import BaseApiTest
from posts.tests.factories import PostFactory
from posts.models import Like


class PostDetailApiTests(BaseApiTest):

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.post = PostFactory()
        cls.url = reverse('posts:post_like', args=[cls.post.id])

    def test_auth_credentials_are_necessary(self):
        self._test_auth_credentials(url=self.url, method='post')

    def test_set_positive_like(self):
        token = self.get_token(email=self.email, password=self.password)
        data = {'kind': True}
        res = self.make_authenticated_request(url=self.url, method='post', jwt_token=token, **data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        like = Like.objects.get(post=self.post, user=self.user)
        self.assertIsNotNone(like)
        self.assertTrue(like.kind)

        res = self.make_authenticated_request(url=self.url, method='post', jwt_token=token, **data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        like = Like.objects.filter(post=self.post, user=self.user).first()
        self.assertIsNone(like)



