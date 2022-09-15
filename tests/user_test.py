import pytest
from . import conftest
from .user import User


def test_first_name(user):

    first_name = user.first_name
    # Expected Pass
    assert first_name == 'jane'


def test_age(user):

    age = User.calculate_age(user)

    # Expected Fail since dob is None
    assert age == 120
