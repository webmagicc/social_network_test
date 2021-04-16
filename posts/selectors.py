from datetime import datetime
from typing import Union

from django.db.models import QuerySet, F, Q, Count

from posts.filters import PostFilter
from posts.models import Post, Like


def post_list(*, filters: Union[dict, None] = None) -> QuerySet:
    filters = filters or {}
    qs = Post.objects.all()
    return PostFilter(filters, qs).qs


def get_post(*, post_id: int) -> Post:
    return Post.objects.get(id=post_id)


def get_or_create_like(*, post_id, user_id) -> Like:
    like, _ = Like.objects.get_or_create(post_id=post_id, user_id=user_id)
    return like


def get_like_analytics(date_from: datetime.date, date_to: datetime.date) -> QuerySet:
    queryset = Like.objects.filter(created_at__date__lte=date_to, created_at__date__gte=date_from)
    queryset = queryset.annotate(day=F('created_at__date'))
    queryset = queryset.values('day')
    queryset = queryset.annotate(likes=Count('id', filter=Q(kind=True)))
    queryset = queryset.annotate(dislikes=Count('id', filter=Q(kind=False)))
    queryset = queryset.values('likes', 'dislikes', 'day')
    return queryset
