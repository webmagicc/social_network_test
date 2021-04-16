from django.test import TestCase

from posts.tests.factories import LikeFactory, PostFactory
from posts.services import set_like
from users.tests.factories import UserFactory
from posts.models import Like


class SetLikeServiceTest(TestCase):

    def setUp(self) -> None:
        self.user = UserFactory()
        self.post = PostFactory()
        self.like = LikeFactory(user=self.user, post=self.post)

    def test_set_like_selector__set_true(self):
        self.assertIsNone(self.like.kind)
        set_like(like=self.like, kind=True)
        self.assertTrue(self.like.kind)

    def test_set_like_selector__set_false(self):
        self.assertIsNone(self.like.kind)
        set_like(like=self.like, kind=False)
        self.assertFalse(self.like.kind)

    def test_set_like_selector__like_removed_on_second_set_true(self):
        self.assertIsNone(self.like.kind)
        set_like(like=self.like, kind=True)
        self.assertTrue(self.like.kind)
        set_like(like=self.like, kind=True)
        self.assertEqual(Like.objects.count(), 0)

    def test_set_like_selector__like_removed_on_second_set_false(self):
        self.assertIsNone(self.like.kind)
        set_like(like=self.like, kind=False)
        self.assertFalse(self.like.kind)
        set_like(like=self.like, kind=False)
        self.assertEqual(Like.objects.count(), 0)




