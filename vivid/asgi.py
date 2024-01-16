import os
from pathlib import Path

import environ
from django.core.asgi import get_asgi_application

BASE_DIR: environ.Path = environ.Path(__file__) - 1
ENV_FILE_DIR: str = os.path.join(BASE_DIR, Path("settings/.env"))

env = environ.Env()
environ.Env.read_env(ENV_FILE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", env("DJANGO_SETTINGS"))

application = get_asgi_application()
