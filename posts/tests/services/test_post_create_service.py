from django.test import TestCase

from posts.services import post_create
from users.tests.factories import UserFactory


class CreatePostServiceTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()
        cls.data = dict(title='test title', text='test text', author=cls.user)

    def test_create_post(self):
        post = post_create(**self.data)
        self.assertEqual(post.title, self.data['title'])
        self.assertEqual(post.text, self.data['text'])
        self.assertEqual(post.author, self.data['author'])
