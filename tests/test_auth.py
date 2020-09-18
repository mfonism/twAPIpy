import requests

import pytest

from twapipy.auth import TwitterBasicAuth


@pytest.mark.usefixtures("mock_post_bearer_token_endpoint")
def test_basic_auth(api_key, api_key_secret, bearer_token):
    response = requests.post(
        "https://api.twitter.com/oauth2/token",
        data={"grant_type": "client_credentials"},
        auth=TwitterBasicAuth(api_key, api_key_secret),
    )
    assert response.json()["access_token"] == bearer_token
