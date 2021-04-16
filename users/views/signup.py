from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from users.services import user_create
from users.models import User


class SignUpView(APIView):
    permission_classes = [AllowAny]

    class InputSerializer(serializers.Serializer):
        email = serializers.EmailField()
        password = serializers.CharField(min_length=8, max_length=20)
        password_repeat = serializers.CharField(min_length=8, max_length=20)
        first_name = serializers.CharField(max_length=50, required=False)
        last_name = serializers.CharField(max_length=50, required=False)

        def validate(self, data):
            if data['password'] != data['password_repeat']:
                raise serializers.ValidationError("Password mismatch")
            return data

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('id', 'email', 'first_name', 'last_name')

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        data.pop('password_repeat')
        user = user_create(**data)
        return Response(self.OutputSerializer(user).data, status=status.HTTP_201_CREATED)
