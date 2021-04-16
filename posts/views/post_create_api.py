from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from posts.models import Post
from posts.services import post_create
from core.mixins import ApiAuthMixin


class PostCreateApi(ApiAuthMixin, APIView):

    class InputSerializer(serializers.Serializer):
        title = serializers.CharField(max_length=255)
        text = serializers.CharField()

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Post
            fields = ('id', 'title', 'text', 'author')

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        data['author'] = request.user
        post = post_create(**data)
        response_data = self.OutputSerializer(post).data
        return Response(response_data, status=status.HTTP_201_CREATED)
