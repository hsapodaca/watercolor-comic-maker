import functools

import fastapi
from fastapi.responses import Response
from fastapi import FastAPI

from hsapodaca.src.watercolor import Watercolor
from hsapodaca.src.xkcd import random_xkcd_comic_id, xkcd, max_xkcd_comic_id

app = FastAPI()


@functools.lru_cache(maxsize=128)
def watercolor(comic_id: int) -> bytes:
    return Watercolor(xkcd(comic_id)).render()


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
    if comic_id <= max_xkcd_comic_id():
        return Response(xkcd(comic_id), media_type="image/png")
    else:
        raise fastapi.HTTPException(
            status_code=fastapi.status.HTTP_404_NOT_FOUND,
            detail="Comic not found")


@app.get('/xkcd/{comic_id}/watercolor')
def show_xkcd_watercolor(comic_id: int):
    if comic_id <= max_xkcd_comic_id():
        return Response(watercolor(comic_id), media_type="image/png")
    else:
        raise fastapi.HTTPException(
            status_code=fastapi.status.HTTP_404_NOT_FOUND,
            detail="Comic not found")
