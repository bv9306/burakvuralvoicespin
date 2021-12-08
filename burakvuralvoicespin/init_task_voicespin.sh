#!/bin/bash

echo "Voicespin settings file is $DJANGO_SETTINGS_MODULE"
set -x
python manage.py migrate --settings=$DJANGO_SETTINGS_MODULE
python ./helperservices/background_processor.py &
python manage.py process_tasks >/dev/null 2>&1 &
python manage.py runserver 0.0.0.0:7000 --settings=$DJANGO_SETTINGS_MODULE