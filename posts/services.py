from typing import Union

from posts.models import Like, Post
from users.models import User


def set_like(*, like: Like, kind: Union[bool, None]):
    """
    Set Kind Like if is not equal old value else delete like instance
    User click like first time - post like
    User click second time - like will remove
    """
    if kind is not None:
        if like.kind != kind:
            like.kind = kind
            like.save()
            return
    like.delete()


def post_create(*, title: str, text: str, author: User) -> Post:
    return Post.objects.create(title=title, text=text, author=author)
