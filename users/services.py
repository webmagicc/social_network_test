from users.models import User


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
