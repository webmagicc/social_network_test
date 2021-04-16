from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from core.mixins import ApiAuthMixin
from posts.models import Post
from posts.selectors import get_post


class PostDetailApi(ApiAuthMixin, APIView):
    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Post
            fields = ('id', 'title', 'text', 'author')

    def get(self, request, post_id):
        post = get_post(post_id=post_id)
        response_data = self.OutputSerializer(post).data
        return Response(response_data)
