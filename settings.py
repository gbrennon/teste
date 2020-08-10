from decouple import config

DEBUG = config('DEBUG', default=False)
PORT = config("PORT", cast=int)
HOST = config("HOST")
GUNICORN_WORKERS = config("GUNICORN_WORKERS", cast=int)
REDIS_HOST = config("REDIS_HOST")
REDIS_PORT = config("REDIS_PORT")