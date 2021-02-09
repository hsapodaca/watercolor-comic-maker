import functools

import fastapi
from fastapi.responses import Response
from fastapi import FastAPI
from typing import Callable
from hsapodaca.src.watercolor import Watercolor
from hsapodaca.src.xkcd import random_xkcd_comic_id, xkcd, max_xkcd_comic_id

app = FastAPI()


# Routes

@app.get('/')
async def index():
    return {'status': 'OK'}


@app.get('/xkcd/random')
def show_xkcd_random():
    return show_xkcd(random_xkcd_comic_id())


@app.get('/xkcd/random/watercolor')
def show_xkcd_random_watercolor():
    return show_xkcd_watercolor(random_xkcd_comic_id())


@app.get('/xkcd/{comic_id}')
def show_xkcd(comic_id: int):
    return load_comic(comic_id, lambda c_id: xkcd(c_id))


@app.get('/xkcd/{comic_id}/watercolor')
def show_xkcd_watercolor(comic_id: int):
    return load_comic(comic_id, lambda c_id: watercolor(c_id))


# Helpers

@functools.lru_cache(maxsize=128)
def watercolor(comic_id: int) -> bytes:
    return Watercolor(xkcd(comic_id)).render()


def load_comic(comic_id: int, transform: Callable[[int], Response]):
    max_id = max_xkcd_comic_id()
    if max_id is None:
        raise fastapi.HTTPException(
            status_code=fastapi.status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Cannot load xkcd")
    elif comic_id > max_id or comic_id < 1:
        raise fastapi.HTTPException(
            status_code=fastapi.status.HTTP_404_NOT_FOUND,
            detail="Comic not found")
    else:
        r = transform(comic_id)
        if r is None:
            raise fastapi.HTTPException(
                status_code=fastapi.status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Cannot load xkcd")
        else:
            return Response(r, media_type="image/png")
