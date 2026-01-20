import unittest

from api.favqs_api_post_request import CreateUser
from api.favqs_api_put_request import GetUserInfo, UpdateUser

from base_tc import BaseTC


class FavQsUserTests(BaseTC):
    def setUp(self):
        super().setUp()

    def test_create_and_get_user(self):
        login = self.generate_login()
        email = self.generate_email()
        password = self.generate_password()

        # Create user
        create_request = CreateUser()
        user_data = {"user": {"login": login, "email": email, "password": password}}
        response, res_json = create_request.execute(data=user_data)
        self.base_request.assert_success_code(response, f"Failed to create user with login {login}")

        user_token = res_json.get("User-Token")
        self.assertIsNotNone(
            user_token,
            f"No User-Token returned after creation of user {login}: {res_json}"
        )

        # Get user info
        get_request = GetUserInfo(user_token=user_token, login=login)
        response, user_info = get_request.execute()
        self.base_request.assert_success_code(response, f"Failed to retrieve user info for {login}")

        self.assertEqual(
            get_request.login_name, login,
            f"Login mismatch. Expected: {login}, Got: {get_request.login_name}"
        )
        self.assertEqual(
            get_request.email, email,
            f"Email mismatch. Expected: {email}, Got: {get_request.email}"
        )

    def test_update_user(self):
        login = self.generate_login()
        email = self.generate_email(login)
        password = self.generate_password()

        # Create user
        create_request = CreateUser()
        user_data = {"user": {"login": login, "email": email, "password": password}}
        response, res_json = create_request.execute(data=user_data)
        self.base_request.assert_success_code(response, f"Failed to create user with login {login}")
        user_token = res_json.get("User-Token")
        self.assertIsNotNone(
            user_token,
            f"No User-Token returned after creation of user {login}: {res_json}"
        )

        # Update user
        new_login = self.generate_login()
        new_email = self.generate_email(new_login)
        update_request = UpdateUser(user_token=user_token, login=login)
        update_data = {"user": {"login": new_login, "email": new_email}}
        response, res_json = update_request.execute(data=update_data)
        self.base_request.assert_success_code(response, f"Failed to update user {login}")

        # Get updated info
        get_request = GetUserInfo(user_token=user_token, login=new_login)
        response, user_info = get_request.execute()
        self.base_request.assert_success_code(response, f"Failed to retrieve updated user info for {new_login}")

        self.assertEqual(
            get_request.login_name, new_login,
            f"Updated login mismatch. Expected: {new_login}, Got: {get_request.login_name}"
        )
        self.assertEqual(
            get_request.email, new_email,
            f"Updated email mismatch. Expected: {new_email}, Got: {get_request.email}"
        )


if __name__ == "__main__":
    unittest.main()
