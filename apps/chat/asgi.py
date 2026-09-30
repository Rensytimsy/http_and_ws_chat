
import os
import sys #use sys (system) to access os system variables
# import modules that support protocols setup for django channels, channels.routing, django.core.asgi, channels.auth, channels.security.websocket   

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack
from chat.routing import urlpatterns as websocket_urlpatterns


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "apps.settings")

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(websocket_urlpatterns)
        )
    )
})