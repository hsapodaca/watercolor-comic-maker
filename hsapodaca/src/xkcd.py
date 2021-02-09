import functools
import json
import random

from typing import Optional

from hsapodaca.src.http import execute_get

xkcd_routes = {
    "recent": "https://xkcd.com/info.0.json",
    "comic": """https://xkcd.com/{}/info.0.json"""
}


def random_xkcd_comic_id() -> int:
    return random.randint(1, max_xkcd_comic_id())


def random_xkcd() -> bytes:
    return xkcd(random_xkcd_comic_id())


@functools.lru_cache(maxsize=128)
def max_xkcd_comic_id() -> Optional[int]:
    r = execute_get(xkcd_routes["recent"])
    if r is None:
        return None
    else:
        json_data = json.loads(r.text)
        max_comic = json_data["num"]
        return max_comic


@functools.lru_cache(maxsize=128)  # todo move to fastapi cache
def xkcd(comic_id: int) -> Optional[bytes]:
    r = execute_get(xkcd_routes["comic"].format(comic_id))
    if r is None:
        return None
    else:
        comic_json = r.text
        img_url = json.loads(comic_json)["img"]
        img_stream = execute_get(img_url, stream=True)
        if img_stream is None:
            return None
        else:
            return img_stream.content
