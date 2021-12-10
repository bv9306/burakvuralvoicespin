#!/bin/bash

echo "Voicespin settings file is $DJANGO_SETTINGS_MODULE"
set -x
python manage.py makemigrations
python manage.py migrate
python /burakvuralvoicespin-test/helper_services/background_processor.py &
python manage.py process_tasks >/dev/null 2>&1 &
gunicorn -c gunicorn_conf.py --preload burakvuralvoicespin.wsgi:application