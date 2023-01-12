from unittest.mock import MagicMock
from unittest import TestCase

from models import User


class TestUser(TestCase):

    def test_new_valid_user(self):
        """
        Test that a new user is created with valid data
        """

        data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "johndoe@gmail.com",
            "uuid": "c0b7f987-72ce-4137-858b-9a380704589c",
            "password": "Password123",
            "birthdate": "1990-01-01"
        }

        user: User = User(**data)

        self.assertTrue(user.is_valid())
