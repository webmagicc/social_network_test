from django.test import TestCase

from posts.tests.factories import PostFactory
from posts.selectors import get_or_create_like
from posts.models import Post
from users.tests.factories import UserFactory


class GetOrCreateLikeSelectorTest(TestCase):

    def setUp(self) -> None:
        self.post = PostFactory()
        self.user = UserFactory()

    def test_post_list_selector(self):
        like = get_or_create_like(user_id=self.user.id, post_id=self.post.id)
        self.assertIsNotNone(like)
        self.assertEqual(self.post, like.post)
        self.assertEqual(self.user, like.user)




