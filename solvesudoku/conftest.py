from authentication.tests import factories as auth_factories
from pytest_factoryboy import register

register(auth_factories.UserFactory)
register(auth_factories.UserSocialAuthFactory)
