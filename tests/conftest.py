import pytest


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
    requests_mock, basic_auth_string, bearer_token
):
    requests_mock.post(
        "https://api.twitter.com/oauth2/token",
        request_headers={
            "Authorization": f"Basic {basic_auth_string}",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        },
        json={"token_type": "bearer", "access_token": f"{bearer_token}"},
    )
