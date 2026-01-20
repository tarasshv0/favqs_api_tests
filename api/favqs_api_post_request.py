from typing import Tuple
import requests
from api.favqs_api_base_request import FavQsAPIBaseRequest


class FavQsAPIPostRequest(FavQsAPIBaseRequest):
    def __init__(self):
        super().__init__()
        self.path = None
        self.data = None

    def execute(self, data: dict = None) -> Tuple[requests.Response, dict]:
        if data:
            self.data = data
        response = requests.post(
            url=f"{self.BASE_URL}{self.path}",
            headers=self.headers,
            json=self.data
        )
        self.assert_not_server_error(response)
        try:
            res_json = response.json()
        except ValueError:
            res_json = {}
        return response, res_json


class CreateUser(FavQsAPIPostRequest):
    def __init__(self):
        super().__init__()
        self.path = "/users"
