from django.urls import path

from users.views import SignUpView


user_patterns = [
    path('signup/', SignUpView.as_view(), name='signup')
]
