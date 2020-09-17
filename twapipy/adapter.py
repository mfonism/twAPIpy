from requests.adapters import HTTPAdapter


class TwitterAdapter(HTTPAdapter):
    def __init__(self, *args, **kwargs):
        super().__init__(max_retries=5)
