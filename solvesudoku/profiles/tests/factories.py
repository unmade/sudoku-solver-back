import factory


class ProfileFactory(factory.DjangoModelFactory):
    name = factory.Faker("name")
    picture_url = factory.Faker("url")

    user = factory.SubFactory(
        "authentication.tests.factories.UserFactory", profile=None
    )

    class Meta:
        model = "profiles.Profile"
