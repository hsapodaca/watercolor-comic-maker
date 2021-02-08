Watercolor Maker
===

Watercolor maker generates watercolor art from a random XKCD comic.

Getting Started
---

    sh run.sh

or

    pip install -r requirements.txt

    export FLASK_ENV=development
    export FLASK_APP=app.py

    flask run ## on port 5000

Afterwards, see the following endpoints:

* http://localhost:5000/xkcd/100
* http://localhost:5000/xkcd/100/watercolor


* http://localhost:5000/xkcd/random
* http://localhost:5000/xkcd/random/watercolor


Details
---

The watercolor effect is achieved using PIL operations: the original image is mirrored, blurred, posterized, and colorized according to color value, then overlayed over the original comic strip.