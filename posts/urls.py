from django.urls import path

from posts.views import PostDetailApi, PostLikeApi, PostListApi, PostCreateApi


post_patterns = [
    path('', PostListApi.as_view(), name='post_list'),
    path('create/', PostCreateApi.as_view(), name='post_create'),
    path('<int:post_id>', PostDetailApi.as_view(), name='post_detail'),
    path('<int:post_id>/like/', PostLikeApi.as_view(), name='post_like'),
]
