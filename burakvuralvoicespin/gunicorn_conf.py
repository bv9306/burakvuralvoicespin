from multiprocessing import cpu_count


def max_workers():
    return cpu_count() * 2 + 1


bind = '0.0.0.0:9000'
max_requests = 1000
worker_class = 'gevent'
workers = max_workers()
