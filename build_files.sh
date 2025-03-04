#!/bin/bash
pip install -r requirements.txt
python3.12.4 manage.py collectstatic --noinput --clear