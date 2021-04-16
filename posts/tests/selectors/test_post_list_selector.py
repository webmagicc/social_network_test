from django.test import TestCase

from posts.tests.factories import PostFactory
from posts.selectors import post_list
from posts.models import Post


class PostListSelectorTest(TestCase):
    count_posts = 5

    def setUp(self) -> None:
        self.posts = PostFactory.create_batch(self.count_posts)

    def test_post_list_selector(self):
        qs = post_list()
        self.assertEqual(qs.count(), self.count_posts)

    def test_post_list_filter_by_title(self):
        post = Post.objects.first()
        qs = post_list(filters={'title': post.title})
        self.assertEqual(qs.count(), 1)

