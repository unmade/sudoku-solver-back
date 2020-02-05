import factory
from faker import Factory as FakerFactory
from social_django.models import UserSocialAuth

from django.contrib.auth import get_user_model


class UserFactory(factory.DjangoModelFactory):
    username = factory.Faker("user_name")
    email = factory.Faker("email")
    first_name = factory.Faker("name")
    password = ""

    class Meta:
        model = get_user_model()
        django_get_or_create = ["username"]


# def extra_data():
#     faker = FakerFactory()
#     return {
#         "auth_time": faker("unix_time"),
#         "expires": faker("int"),
#         "token_type": "Bearer",
#         "access_token": faker("sha256"),
#         "picture": faker("url"),
#     }


class UserSocialAuthFactory(factory.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    provider = "google-oauth2"
    # extra_data = {
    #     "auth_time": factory.Faker("unix_time"),
    #     "expires": factory.Faker("int"),
    #     "token_type": "Bearer",
    #     "access_token": factory.Faker("sha256"),
    #     "picture": factory.Faker("url"),
    # }

    class Meta:
        model = UserSocialAuth

    @factory.post_generation
    def uid(self, *args, **kwargs):
        self.uid = self.user.email
        self.save(update_fields=["uid"])

    @factory.post_generation
    def extra_data(self, *args, **kwargs):
        faker = FakerFactory.create()
        self.extra_data = {
            "auth_time": faker.unix_time(),
            "expires": faker.pyint(),
            "token_type": "Bearer",
            "access_token": faker.sha256(),
            "name": self.user.first_name,
            "picture": faker.url(),
        }
        self.save(update_fields=["extra_data"])
