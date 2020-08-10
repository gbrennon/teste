from settings import PORT, HOST, GUNICORN_WORKERS

bind = f"{HOST}:{PORT}"
workers = GUNICORN_WORKERS
worker_class = "gevent"
worker_connections = 1000
mas_request = int(workers * worker_connections)
keepalive = 2
max_request_jitter = 5
timeout = 30
errorlog = "-"
