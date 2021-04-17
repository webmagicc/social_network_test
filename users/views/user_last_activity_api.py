from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from core.mixins import ApiAuthMixin
from posts.models import Post
from users import services, selectors


class UserLastActivityApi(ApiAuthMixin, APIView):
    class OutputSerializer(serializers.Serializer):
        last_login_date = serializers.DateTimeField(required=False, allow_null=True)
        last_request_date = serializers.DateTimeField(required=False, allow_null=True)
        last_request_url = serializers.CharField(required=False)

    def get(self, request):
        last_activity = selectors.get_last_activity(user=request.user)
        data = services.get_user_last_activity_data(user=request.user, last_activity=last_activity)
        return Response(self.OutputSerializer(data).data)
