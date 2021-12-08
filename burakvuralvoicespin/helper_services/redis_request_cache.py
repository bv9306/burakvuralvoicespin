import json
import uuid

import redis

redis_host = "192.168.48.1"
redis_port = 6379
redis_password = ""
red_client = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)


def write_request_to_redis(request):
    red_client.rpush(str(uuid.uuid4()), json.dumps(request.data))

