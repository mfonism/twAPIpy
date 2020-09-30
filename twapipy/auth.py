import base64

import requests


class TwitterAuthBase(requests.auth.AuthBase):
    auth_url = "https://api.twitter.com/oauth2/token"

    def __init__(self, api_key, api_key_secret):
        self._api_key = api_key
        self._api_key_secret = api_key_secret


class TwitterBasicAuth(TwitterAuthBase):
    def __init__(self, api_key, api_key_secret):
        super().__init__(api_key, api_key_secret)
        self._basic_auth_string = self._get_basic_auth_string()

    def _get_basic_auth_string(self):
        cred = f"{self._api_key}:{self._api_key_secret}"
        return base64.b64encode(cred.encode("utf-8")).decode("utf-8")

    def __call__(self, r):
        r.headers["Authorization"] = "Basic " + self._basic_auth_string
        r.headers["Content-Type"] = "application/x-www-form-urlencoded;charset=UTF-8"
        return r


class TwitterBearerAuth(TwitterAuthBase):
    _post_data = {"grant_type": "client_credentials"}

    def __init__(self, api_key, api_key_secret):
        super().__init__(api_key, api_key_secret)
        self._access_token = None

    def _get_access_token(self):
        try:
            response = requests.post(
                self.auth_url,
                json=self._post_data,
                auth=TwitterBasicAuth(self._api_key, self._api_key_secret),
            )
            return response.json()["access_token"]
        except Exception as e:
            raise Exception(f"Error fetching access token: {e}")

    def __call__(self, r):
        self.ensure_access_token()
        r.headers["Authorization"] = "Bearer " + self._access_token
        return r

    def ensure_access_token(self):
        if self._access_token is not None:
            return
        self._access_token = self._get_access_token()

    def get_post_data(self):
        return self._post_data
