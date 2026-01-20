from typing import Tuple
import requests
from api.favqs_api_base_request import FavQsAPIBaseRequest


class FavQsAPIPutRequest(FavQsAPIBaseRequest):
    def __init__(self, user_token: str = None):
        super().__init__()
        if user_token:
            self.headers["User-Token"] = user_token
        self.path = None
        self.data = None

    def execute(self, data: dict = None) -> Tuple[requests.Response, dict]:
        if data:
            self.data = data
        response = requests.put(
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


class GetUserInfo(FavQsAPIBaseRequest):
    def __init__(self, user_token: str, login: str):
        super().__init__()
        self.headers["User-Token"] = user_token
        self.login = login
        self.email = None
        self.login_name = None

    def execute(self) -> Tuple[requests.Response, dict]:
        url = f"{self.BASE_URL}/users/{self.login}"
        response = requests.get(url, headers=self.headers)
        self.assert_not_server_error(response)
        try:
            res_json = response.json()
        except ValueError:
            res_json = {}
        account_details = res_json.get("account_details", {})
        self.email = account_details.get("email")
        self.login_name = res_json.get("login")
        return response, res_json


class UpdateUser(FavQsAPIPutRequest):
    def __init__(self, user_token: str, login: str):
        super().__init__(user_token=user_token)
        self.path = f"/users/{login}"
