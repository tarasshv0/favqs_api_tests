import os
import unittest
import random
import string

from api.favqs_api_base_request import FavQsAPIBaseRequest


class BaseTC(unittest.TestCase):
    """Base test case class for FavQs API tests"""

    def setUp(self):
        super().setUp()
        self.api_key = os.environ.get("FAVQS_API_KEY")
        self.base_request = FavQsAPIBaseRequest()

    def generate_random_string(self, length: int = 8) -> str:
        """Generate a random string"""
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

    def generate_email(self, login: str = None) -> str:
        """Generate a test email"""
        if login is None:
            login = self.generate_random_string()
        return f"{login}@test.com"

    def generate_login(self) -> str:
        """Generate a test login"""
        return f"test_user_{self.generate_random_string()}"

    def generate_password(self, length: int = 12) -> str:
        """Generate a random password with letters, digits and punctuation"""
        chars = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choices(chars, k=length))
