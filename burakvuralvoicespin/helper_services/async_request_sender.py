import asyncio
import json
import logging
import time
from datetime import datetime
from multiprocessing import Process
import multiprocessing

import aiohttp

logger = logging.getLogger(__name__)

processes = []


async def send_request_to_callback(duration, start_time, callback_url):
    async with aiohttp.ClientSession() as session:
        try:
            print(f'Trying to send request {callback_url}')
            logger.info(f'Trying to send request {callback_url}')
            headers = {'Content-Type': 'application/json'}
            duration = {"duration": duration, "start_time": start_time, "end_time": str(datetime.utcnow()),
                        "calculation_operation_status": "completed"}
            async with session.post(callback_url, data=json.dumps(duration), headers=headers) as resp:
                await resp.json(content_type=None)
        except Exception:
            logger.exception('While sending request to have been observed')


def make_heavy_operation(redis_value_list):
    try:
        processes.append(Process(target=calculate, args=(redis_value_list[0],)))
    except Exception as e:
        print(e)
        logger.exception(e)
        return e


def calculate(redis_value):
    time.sleep(15)
    redis_value_str = redis_value
    redis_value_json = json.loads(redis_value_str)
    return asyncio.run(send_request_to_callback(redis_value_json['duration'], redis_value_json['start_time'],
                                                redis_value_json['callback_url']))
