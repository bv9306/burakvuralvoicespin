"""
WSGI config for burakvuralvoicespin project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

from django.conf import settings

if settings.IS_MONKEY_ENABLED:
    from gevent import monkey
    monkey.patch_all()

import os

from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'burakvuralvoicespin.settings')

application = get_wsgi_application()
