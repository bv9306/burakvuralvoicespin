import json
import uuid

import redis

redis_host = "192.168.48.1"
redis_port = 6379
redis_password = ""
red_client = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)


def write_request_to_redis(request):
    red_client.rpush(str(uuid.uuid4()), json.dumps(request.data))
    keys = red_client.keys()
    print("-----------------------------")
    for key in keys:
        type = red_client.type(key)
        if type == "list":
            value = red_client.lrange(key, 0, -1)
            print(key)
            print(value)
        #red_client.delete(key)
