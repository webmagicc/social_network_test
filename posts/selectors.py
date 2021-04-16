from typing import Union

from django.db.models import QuerySet

from posts.filters import PostFilter
from posts.models import Post, Like


def post_list(*, filters: Union[dict, None] = None) -> QuerySet:
    filters = filters or {}
    qs = Post.objects.all()
    return PostFilter(filters, qs).qs


def get_post(*, post_id: int) -> Post:
    return Post.objects.get(id=post_id)


def get_or_create_like(*, post_id, user_id):
    like, _ = Like.objects.get_or_create(post_id=post_id, user_id=user_id)
    return like
