import requests
from typing import Optional

from fastapi.openapi.models import Response
from requests.adapters import HTTPAdapter
from urllib3 import Retry


def execute_get(path: str, stream: bool = False) -> Optional[Response]:
    retry_strategy = Retry(
        total=3,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["HEAD", "GET", "OPTIONS"]
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    s = requests.Session()
    s.mount("http://", adapter)
    r = s.get(path, stream=stream)
    if r.status_code == 200:
        return r
    else:
        return None
