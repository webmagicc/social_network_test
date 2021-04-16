from django.urls import reverse
from rest_framework import status

from core.tests import BaseApiTest
from posts.models import Post


class PostCreateApiTests(BaseApiTest):

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.url = reverse('posts:post_create')
        cls.data = dict(title='test title', text='test text')

    def test_auth_credentials_are_necessary(self):
        self._test_auth_credentials(url=self.url, method='post')

    def test_post_create(self):
        token = self.get_token(email=self.email, password=self.password)
        res = self.make_authenticated_request(url=self.url, method='post', jwt_token=token, **self.data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        post = Post.objects.filter(author=self.user).first()
        self.assertIsNotNone(post)
        self.assertEqual(post.title, self.data['title'])



