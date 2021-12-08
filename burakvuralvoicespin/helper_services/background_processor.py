
import os


import django
from background_task import background

from burakvuralvoicespin.helper_services.async_request_sender import make_heavy_operation

os.environ['DJANGO_SETTINGS_MODULE'] = 'burakvuralvoicespin.settings'

django.setup()

from burakvuralvoicespin.helper_services.redis_request_cache import red_client


def evaluate_heavy_operations_request_to_database():
    while True:
        keys = red_client.keys()
        if keys is not None:
            for key in keys:
                type = red_client.type(key)
                if type == "list":
                    value = red_client.lrange(key, 0, -1)
                    make_heavy_operation(value)
                    red_client.delete(key)


evaluate_heavy_operations_request_to_database()
