import json
import os
import uuid

import redis

redis_host = os.environ['REDIS_HOST']
redis_port = os.environ['REDIS_PORT']
redis_password = ""
red_client = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)


def write_request_to_redis(request):
    red_client.rpush(str(uuid.uuid4()), json.dumps(request.data))

