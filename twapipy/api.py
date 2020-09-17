import requests

from .adapter import TwitterAdapter
from .bearer_auth import TwitterBearerAuth


class TwitterOAuth2API:
    api_url = "https://api.twitter.com/"

    def __init__(self, api_key, api_key_secret):
        self.auth = TwitterBearerAuth(api_key, api_key_secret)

    def get(self, endpoint, params=None):
        with requests.Session() as session:

            url = self.api_url + endpoint

            session.auth = self.auth
            session.mount(self.api_url, TwitterAdapter())

            return session.get(url, params=params, timeout=(5, 5))
