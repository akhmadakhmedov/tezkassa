from kassa.settings.base import *


DEBUG = True

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles/")

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]
