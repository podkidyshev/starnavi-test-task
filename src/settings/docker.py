DEBUG = False
ALLOWED_HOSTS = []

try:
    from .local_settings import *
except ImportError:
    pass
