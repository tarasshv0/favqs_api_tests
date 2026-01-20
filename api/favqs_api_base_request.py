import requests
from requests import Response
from config import FAVQS_API_KEY
from config import BASE_URL


class FavQsAPIBaseRequest:
    BASE_URL = BASE_URL

    def __init__(self):
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f'Token token="{FAVQS_API_KEY}"'
        }
        self.success_codes = [
            requests.codes.ok,
            requests.codes.created,
            requests.codes.accepted,
            requests.codes.no_content
        ]

    def assert_success_code(self, response: Response, message: str):
        assert response.status_code in self.success_codes, \
            f"{message}. Status code: {response.status_code}, Response: {response.text}"

    def assert_not_server_error(self, response: Response):
        assert response.status_code < 500, \
            f"Server error. Status code: {response.status_code}, Response: {response.text}"
