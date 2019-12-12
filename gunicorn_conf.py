import json
import multiprocessing
import os

workers_per_core_str = os.getenv("GUNICORN_WORKERS_PER_CORE", "1")
web_concurrency_str = os.getenv("GUNICORN_WORKERS", None)
threads_str = os.getenv("GUNICORN_THREADS", "1")
host = os.getenv("HOST", "0.0.0.0")
port = os.getenv("PORT", "8000")
bind_env = os.getenv("GUNICORN_BIND", None)
use_loglevel = os.getenv("GUNICORN_LOG_LEVEL", "info")
if bind_env:
    use_bind = bind_env
else:
    use_bind = f"{host}:{port}"

cores = multiprocessing.cpu_count()
workers_per_core = float(workers_per_core_str)
default_web_concurrency = workers_per_core * cores
if web_concurrency_str:
    web_concurrency = int(web_concurrency_str)
    assert web_concurrency > 0
else:
    web_concurrency = max(int(default_web_concurrency), 2)

# Gunicorn config variables
bind = use_bind
workers = web_concurrency
preload_app = True
reuse_port = True
threads = int(threads_str)
keepalive = 120

loglevel = use_loglevel
accesslog = "-"
errorlog = "-"

# For debugging and testing
log_data = {
    "loglevel": loglevel,
    "workers": workers,
    "bind": bind,
    # Additional, non-gunicorn variables
    "workers_per_core": workers_per_core,
    "host": host,
    "port": port,
}
print(json.dumps(log_data))
