from vivid.settings.base import *

SECRET_KEY: str = env("SECRET_KEY")

DEBUG: bool = False

CORS_ORIGIN_ALLOW_ALL: bool = True
CORS_ORIGIN_WHITELIST: list[str] = []

ALLOWED_HOSTS: list[str] = []
