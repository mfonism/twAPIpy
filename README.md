# twAPIpy

twAPIpy _/twʌpi pʌɪ/_

A simple project for teaching how to make API calls with Python like a pro.


# Usage

```Python
from twapipy import TwAPI

# your Twitter API keys as obtained from your Twitter developer account
API_KEY = "<insert>"
API_KEY_SECRET = "<insert>"

api = TwAPI(API_KEY, API_KEY_SECRET)

# make a get request to
# https://api.twitter.com/2/tweets/search/recent?query=python&max_results=100
# note that the endpoint you supply should not include 'https://api.twitter.com'
# also note that it should start with a slash
response = api.get(
    "/2/tweets/search/recent",
    params={"query": "python", "max_results": "100"}
)
response_data = response.json()["data"]
...
```