#!/usr/bin/sh

wget https://raw.githubusercontent.com/AlexandreDecan/genja/master/genja.py
wget https://raw.githubusercontent.com/AlexandreDecan/genja/master/requirements.txt
pip install -r requirements.txt
python genja.py
