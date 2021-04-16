from factory.django import DjangoModelFactory
import factory


class UserFactory(DjangoModelFactory):
    class Meta:
        model = "users.User"

    email = factory.Faker('email')
