# SECOHealth sources

[![Build Status](https://travis-ci.org/secohealth/secohealth.github.io.svg?branch=sources)](https://travis-ci.org/secohealth/secohealth.github.io)

Do **not** make modifications to the master branch!
Feel free to make your modifications on this branch. 
Any commit (that ends in a valid set of files) will automatically trigger the build and deployment of the website. 

The website is built with [Genja](https://github.com/AlexandreDecan/Genja), a minimalist static website generator written specifically for SECOHealth. It is built on top of [Jinja2](https://jinja.pocoo.org/docs/latest/), a powerful template engine written in Python. The layout of the website relies on [Bootstrap 3](https://getbootstrap.com/docs/3.3/). 

If you want to locally test your modifications before pushing them, go to the Genja repository and download both ``genja.py`` and ``requirements.txt``. The script requires Python >= 3.4, and some dependencies that can be easily installed using ``pip install -r requirements.txt``. Then simply type ``python genja.py`` at the root of this repository to build the pages. 
