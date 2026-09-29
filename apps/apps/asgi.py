

import os
import sys
import pysqlite3

sys.modules["sqlite3"] = sys.modules.pop("pysqlite3")

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'apps.settings')

application = get_asgi_application()
