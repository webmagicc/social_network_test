from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from posts.models import Post
from posts.selectors import post_list
from core.pagination import get_paginated_response, LimitOffsetPagination
from core.mixins import ApiAuthMixin


class PostListApi(ApiAuthMixin, APIView):

    class InputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Post
            fields = ('title', 'text')

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Post
            fields = ('id', 'title', 'text', 'author')

    class FilterSerializer(serializers.Serializer):
        title = serializers.CharField(max_length=255, required=False)
        author_name = serializers.CharField(max_length=20, required=False)
        author_email = serializers.CharField(max_length=20, required=False)
        id = serializers.IntegerField(required=False)

    def get(self, request):
        filters_serializer = self.FilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        users = post_list(filters=filters_serializer.validated_data)

        return get_paginated_response(
            pagination_class=LimitOffsetPagination,
            serializer_class=self.OutputSerializer,
            queryset=users,
            request=request,
            view=self
        )

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        post = serializer.save(author=request.user)
        response_data = self.OutputSerializer(post).data
        return Response(response_data, status=status.HTTP_201_CREATED)
