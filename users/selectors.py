from users.models import User, UserLastActivity


def get_last_activity(*, user: User) -> UserLastActivity:
    last_activity, _ = UserLastActivity.objects.get_or_create(user=user)
    return last_activity
