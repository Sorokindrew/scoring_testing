import time

import redis
from redis.exceptions import ConnectionError, TimeoutError


class Store:
    def __init__(self, retries: int = 5, timeout: int = 1):
        self._conn = None
        self._retries = retries
        self._timeout = timeout

    def connect(self):
        try:
            self._conn = redis.Redis(
                host="localhost",
                port=6379,
                db=0,
                socket_timeout=self._timeout,
            )
            self._conn.ping()
        except (ConnectionError, TimeoutError) as e:
            self._conn = None

    def reconnect(self):
        while self._conn is None and self._retries:
            print("try reconnect...")
            self.connect()
            if self._conn is None:
                self._retries -= 1
                time.sleep(5)

    def cache_set(self, key, value, cache_time):
        try:
            self._conn.setex(key, cache_time, value)
        except (ConnectionError, TimeoutError):
            self.reconnect()
            self._conn.setex(key, cache_time, value)

    def cache_get(self, key):
        try:
            return self._conn.get(key)
        except (ConnectionError, TimeoutError):
            self.reconnect()
            return self._conn.get(key)

    def get(self, key):
        try:
            return self._conn.get(key)
        except (ConnectionError, TimeoutError):
            self.reconnect()
            return self._conn.get(key)