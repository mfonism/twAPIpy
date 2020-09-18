# twAPIpy

twAPIpy _/twʌpi pʌɪ/_

A simple project for teaching how to make API calls with Python like a pro.


# Usage

```Python
from twapipy.api import TwitterOAuth2API as TwAPI


API_KEY = '<insert your twitter api key here>'
API_KEY_SECRET = '<insert your twitter api key secret here>'
# alternatively, you can read them from a dot env file

api = TwAPI(API_KEY, API_KEY_SECRET)

# make a get request to
# https://api.twitter.com/2/tweets/search/recent?query=python&max_results=100
response = api.get('2/tweets/search/recent', params={'query':'python', 'max_results':100})
response_data = response.json()['data']
...
```