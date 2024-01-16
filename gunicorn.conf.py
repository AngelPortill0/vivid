bind = "localhost"
backlog = 2048
workers = 4
timeout = 45
keepalive = 5
errorlog = "/var/log/gunicorn/gunicorn.error.log"
accesslog = "/var/log/gunicorn/gunicorn.access.log"
loglevel = "info"
