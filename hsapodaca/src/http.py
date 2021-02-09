import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry


def execute_get(path, stream=False):
    retry_strategy = Retry(
        total=3,
        status_forcelist=[429, 500, 502, 503, 504],
        method_whitelist=["HEAD", "GET", "OPTIONS"]
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    s = requests.Session()
    s.mount("http://", adapter)
    return s.get(path, stream=stream)



