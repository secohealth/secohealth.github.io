# SECOHealth sources

[![Build Status](https://travis-ci.org/secohealth/secohealth.github.io.svg?branch=sources)](https://travis-ci.org/secohealth/secohealth.github.io)

This website is built with [Genja](https://github.com/AlexandreDecan/Genja), a minimalist static website generator written specifically for SECOHealth. It is built on top of [Jinja2](https://jinja.pocoo.org/docs/latest/), a powerful template engine written in Python. The layout of the website relies on [Bootstrap 3](https://getbootstrap.com/docs/3.3/). 

Any modification or pull request should be done on the "sources" branch. Please note that NO modification should be done on the "master" branch on GitHub. Every commit done in the sources branch triggers an automatic build (thanks to Travis-CI) by Genja, and an automatic deployment to GitHub pages (ie. the content of the output folder will be copied as-is to the master branch). Notice that any "invalid" modification (ie. any modifications that lead to something that cannot be processed by Genja) will not be deployed. The "build status" badge informs you of the status of the latest build. 

If you want to locally test your modifications before pushing them, go to the Genja repository and download both ``genja.py`` and ``requirements.txt``. The script requires Python >= 3.4, and some dependencies that can be easily installed using ``pip install -r requirements.txt``. Then simply type ``python genja.py`` at the root of this repository to build the pages. 
