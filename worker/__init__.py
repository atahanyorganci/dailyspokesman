import redis
from decouple import config
from rq import Worker, Queue, Connection

REDIS_URL = config('REDIS_TLS_URL', default=None)
if REDIS_URL is None:
    REDIS_URL = config('REDIS_URL')

listen = ['high', 'default', 'low']
connection = redis.from_url(REDIS_URL)

if __name__ == '__main__':
    with Connection(connection):
        worker = Worker(map(Queue, listen))
        worker.work()
