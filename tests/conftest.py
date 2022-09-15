import pytest
from .user import User


@pytest.fixture(scope='module')
def user():

    user = User("jane", "doe", "email", "password")
    yield user
