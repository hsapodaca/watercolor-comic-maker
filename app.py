import functools

from flask import Flask

from hsapodaca.src.watercolor import Watercolor
from hsapodaca.src.http import make_png_response
from hsapodaca.src.xkcd import random_xkcd_comic_id, xkcd

app = Flask(__name__)


@functools.lru_cache(maxsize=128)
def watercolor(comic_id: int) -> bytes:
    return Watercolor(xkcd(comic_id)).render()


@app.route('/')
def index():
    return 'OK'


@app.route('/xkcd/random', methods=['GET'])
def show_xkcd_random():
    return show_xkcd(random_xkcd_comic_id())


@app.route('/xkcd/random/watercolor', methods=['GET'])
def show_xkcd_random_watercolor():
    return show_xkcd_watercolor(random_xkcd_comic_id())


@app.route('/xkcd/<int:comic_id>', methods=['GET'])
def show_xkcd(comic_id):
    return make_png_response(xkcd(comic_id))


@app.route('/xkcd/<int:comic_id>/watercolor', methods=['GET'])
def show_xkcd_watercolor(comic_id):
    return make_png_response(watercolor(comic_id))
