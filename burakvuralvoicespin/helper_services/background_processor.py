import time

from background_task import background

from async_request_sender import make_heavy_operation, processes
from redis_request_cache import red_client


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

def evaluate_processes_at_cron():
    while True:
        time.sleep(5)
        if processes is not None and len(processes) > 0:
            for process in processes:
                process.start()
            for process in processes:
                process.join()
                print('registering next process')
                processes.remove(process)


evaluate_heavy_operations_request_to_database()
evaluate_processes_at_cron()
