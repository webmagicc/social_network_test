from datetime import datetime
from typing import TypedDict

from users.models import User, UserLastActivity


def user_create(
        *,
        email: str,
        password: str,
        first_name: str = "",
        last_name: str = ""
) -> User:
    user = User.objects.create_user(
        email=email, password=password, first_name=first_name, last_name=last_name
    )
    return user


def set_user_last_activity(*, user: User, url: str):
    if 'api' in url:
        last_activity, _ = UserLastActivity.objects.get_or_create(user=user)
        last_activity.url = url
        last_activity.save()


class LastActivityData(TypedDict):
    last_login_date: datetime
    last_request_date: datetime
    last_request_url: str


def get_user_last_activity_data(*, user: User, last_activity: UserLastActivity) -> LastActivityData:
    res: LastActivityData = {
        'last_login_date': user.last_login,
        'last_request_date': last_activity.created_at,
        'last_request_url': last_activity.url
    }
    return res
