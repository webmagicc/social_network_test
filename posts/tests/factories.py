from factory.django import DjangoModelFactory
import factory

from users.tests.factories import UserFactory


class PostFactory(DjangoModelFactory):
    class Meta:
        model = "posts.Post"

    author = factory.SubFactory(UserFactory)
    title = factory.Faker('name')
    text = factory.Faker('text')


class LikeFactory(DjangoModelFactory):
    class Meta:
        model = "posts.Like"

    user = factory.SubFactory(UserFactory)
    post = factory.SubFactory(PostFactory)

