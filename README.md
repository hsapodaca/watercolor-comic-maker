Watercolor Maker
===

Watercolor maker generates watercolor art from a random XKCD comic.

Getting Started
---

    sh run.sh


Afterwards, see the following endpoints:

* /xkcd/100
* /xkcd/100/watercolor


* /xkcd/random
* /xkcd/random/watercolor

* /docs

Details
---

The watercolor effect is achieved using PIL operations: the original image is mirrored, blurred, posterized, and colorized according to color value, then overlayed over the original comic strip.