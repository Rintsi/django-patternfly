#!/bin/bash

cd ..
./build.sh
cd example
python manage.py runserver