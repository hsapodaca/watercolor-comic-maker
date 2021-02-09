import io
import random

from PIL import Image, ImageOps, ImageFilter


def random_color():
    colors = ["firebrick", "brown", "maroon", "crimson", "red", "yellow", "green", "blue", "olive",
              "orangered", "darkorange", "darkolivegreen", "forestgreen", "coral", "lavender", "lime",
              "lightseagreen", "teal", "deepskyblue", "steelblue", "dodgerblue",
              "royalblue", "blue", "blueviolet", "indigo", "darkviolet", "purple"]
    return colors[random.randint(0, len(colors) - 1)]


class Watercolor:

    def __init__(self, img: bytes):
        self.img: Image = Image.open(io.BytesIO(img)).convert("RGB")
        self.DEFAULT_BLEND_RATIO = .5

    def blend_with(self, img2: Image) -> Image:
        return Image.blend(self.img, img2, self.DEFAULT_BLEND_RATIO)

    def background_from_image(self) -> Image:
        inverse_img = ImageOps.posterize(ImageOps.mirror(self.img.filter(ImageFilter.GaussianBlur(15))), 3)
        color_img = ImageOps.colorize(inverse_img.convert("L"), black=random_color(), white=random_color())
        final_img = Image.blend(inverse_img, color_img, self.DEFAULT_BLEND_RATIO)
        return final_img

    def effect_overlay(self) -> Image:
        bg_img = self.background_from_image()
        final_img = self.blend_with(bg_img)
        return final_img

    def render(self) -> bytes:
        watercolor_img: Image = self.effect_overlay()
        buf = io.BytesIO()
        watercolor_img.save(buf, format='PNG')
        byte_im = buf.getvalue()
        return byte_im
