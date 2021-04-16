from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from posts import selectors, services
from core.mixins import ApiAuthMixin


class PostLikeApi(ApiAuthMixin, APIView):

    class InputSerializer(serializers.Serializer):
        kind = serializers.NullBooleanField()

    def post(self, request, post_id):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        like = selectors.get_or_create_like(post_id=post_id, user_id=request.user.id)
        services.set_like(like=like, kind=data['kind'])
        return Response(status=status.HTTP_201_CREATED)
