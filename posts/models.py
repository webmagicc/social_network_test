from django.db import models

from core.models import CreatedUpdatedModel


class Post(CreatedUpdatedModel):
    title = models.CharField(max_length=255, default="", db_index=True)
    text = models.TextField(default="")

    author = models.ForeignKey("users.User", on_delete=models.CASCADE)


class Like(CreatedUpdatedModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    kind = models.BooleanField(default=None, null=True, help_text="True = Like | False = Dislike")
