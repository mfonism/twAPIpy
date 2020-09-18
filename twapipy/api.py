import requests

from .adapter import TwitterAdapter
from .bearer_auth import TwitterBearerAuth


class TwitterOAuth2API:
    api_url = "https://api.twitter.com"

    def __init__(self, api_key, api_key_secret):
        self.auth = TwitterBearerAuth(api_key, api_key_secret)

    def request(self, method, endpoint, **kwargs):
        with requests.Session() as session:

            url = self.api_url + endpoint

            session.auth = self.auth
            session.mount(self.api_url, TwitterAdapter())

            kwargs.setdefault("timeout", (5, 5))

            return session.request(method, url, **kwargs)

    def get(self, endpoint, **kwargs):
        return self.request("GET", endpoint, **kwargs)
