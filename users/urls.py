from django.urls import path

from users.views import SignUpView, UserLastActivityApi


user_patterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('last_activity/', UserLastActivityApi.as_view(), name='last_activity')
]
