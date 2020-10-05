import json

import pytest
import requests


@pytest.fixture(name="api_key")
def fixture_api_key():
    # if this is ever changed, then fixture `basic_auth_string` **must** be recomputed
    return "0"


@pytest.fixture(name="api_key_secret")
def fixture_api_key_secret():
    # if this is ever changed, then fixture `basic_auth_string` **must** be recomputed
    return "1"


@pytest.fixture(name="basic_auth_string")
def fixture_basic_auth_string():
    # this **must** be recomputed whenever any of the fixtures
    # `api_key` and `api_key_secret` changes
    return "MDox"


@pytest.fixture(name="bearer_token")
def fixture_bearer_token():
    # doesn't mean much, was taken off of twitter's documentation
    return "AAAA%2FAAA%3DAAAAAAAA"


@pytest.fixture(name="mock_post_bearer_token_endpoint")
def fixture_mock_post_bearer_token_endpoint(
    requests_mock, basic_auth_string, bearer_token, forbidden_response
):
    def matcher(req):
        if req.path != "/oauth2/token":
            return None
        if req.headers.get("Authorization") != f"Basic {basic_auth_string}":
            return forbidden_response
        if (
            req.headers.get("Content-Type")
            != "application/x-www-form-urlencoded;charset=UTF-8"
        ):
            return forbidden_response
        if req.json().get("grant_type") != "client_credentials":
            return forbidden_response

        resp = requests.Response()
        resp._content = json.dumps(
            {"token_type": "bearer", "access_token": f"{bearer_token}"}
        ).encode()
        resp.status_code = 200

        return resp

    requests_mock._adapter.add_matcher(matcher)
    yield


@pytest.fixture(name="forbidden_response")
def fixture_forbidden_response():
    resp = requests.Response()
    resp.status_code = 403
    return resp


@pytest.fixture(name="mock_json_from_api_get_endpoint")
def fixture_mock_json_from_api_get_endpoint():
    return {
        "data": [
            {"id": "123456789", "text": "Python 2 is dead, long live Python 3!"},
            {"id": "543212345", "text": "Python rocks."},
            {"id": "333666999", "text": "TIL python is not always a snake."},
        ]
    }


@pytest.fixture(name="mock_api_get_endpoint")
def fixture_mock_api_get_endpoint(
    requests_mock, bearer_token, mock_json_from_api_get_endpoint
):
    requests_mock.get(
        "https://api.twitter.com/2/tweets/search/recent?query=python&max_results=3",
        request_headers={"Authorization": f"Bearer {bearer_token}"},
        json=mock_json_from_api_get_endpoint,
    )
