import functools
import json
import random

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
def max_xkcd_comic_id() -> int:
    r = execute_get(xkcd_routes["recent"])
    json_data = json.loads(r.text)
    max_comic = json_data["num"]
    return max_comic


@functools.lru_cache(maxsize=128)
def xkcd(comic_id: int) -> bytes:
    comic_json = execute_get(xkcd_routes["comic"].format(comic_id)).text
    img_url = json.loads(comic_json)["img"]
    img_stream = execute_get(img_url, stream=True)
    return img_stream.content
