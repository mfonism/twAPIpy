import pytest

from twapipy import TwAPI


@pytest.mark.usefixtures(
    "requests_mock", "mock_post_bearer_token_endpoint", "mock_api_get_endpoint"
)
def test_api_get_endpoint(api_key, api_key_secret, mock_json_from_api_get_endpoint):
    api = TwAPI(api_key, api_key_secret)
    response = api.get(
        "/2/tweets/search/recent", params={"max_results": "3", "query": "python"}
    )
    assert response.json() == mock_json_from_api_get_endpoint
