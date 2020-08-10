import logging
import pickle
from typing import Union, Tuple

from redis import ConnectionPool, Redis
from redis.exceptions import RedisError

from settings import REDIS_HOST, REDIS_PORT


class RedisServer:

    connection_pool = None
    redis = None

    def __init__(self):
        self.__set_connection_pool()
        self.__set_redis_server()

    def __set_connection_pool(self) -> None:
        self.connection_pool = ConnectionPool(
            host=REDIS_HOST,
            port=REDIS_PORT,
            db=0
        )

    def __set_redis_server(self) -> None:
        self.redis = Redis(connection_pool=self.connection_pool)

    def get_redis_server(self) -> object:
        return self.redis

    def get(self, *args: Tuple, **kwargs: object) -> Union[str, None]:
        try:
            result = self.redis.get(*args, **kwargs)
            if result:
                return pickle.loads(result)
            return None
        except RedisError as e:
            logging.error(e)
            return None

    def set(self, *args: Tuple, **kwargs: object) -> Union[str, None]:
        try:
            kwargs["value"] = pickle.dumps(kwargs["value"])
            return self.redis.set(*args, **kwargs)
        except RedisError as e:
            logging.error(e)
            return None


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Cache(RedisServer, metaclass=Singleton):
    pass
