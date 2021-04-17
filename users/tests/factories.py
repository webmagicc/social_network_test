from factory.django import DjangoModelFactory
import factory


class UserFactory(DjangoModelFactory):
    class Meta:
        model = "users.User"

    email = factory.Faker('email')


class UserLastActivityFactory(DjangoModelFactory):
    class Meta:
        model = "users.UserLastActivity"

    user = factory.SubFactory(UserFactory)
    url = factory.Faker('url')
