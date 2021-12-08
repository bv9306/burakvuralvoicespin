import asyncio
import json
import logging

import aiohttp

logger = logging.getLogger(__name__)


async def send_request_to_callback(duration, callback_url):
    async with aiohttp.ClientSession() as session:
        try:
            print(f'Trying to send request {callback_url}')
            headers = {'Content-Type': 'application/json'}
            duration = {"duration": duration}
            async with session.post(callback_url, data=json.dumps(duration), headers=headers) as resp:
                await resp.json(content_type=None)
        except Exception:
            logger.exception('While sending request to have been observed')


def make_heavy_operation(request, callback_url):
    return asyncio.run(send_request_to_callback(request, callback_url))
