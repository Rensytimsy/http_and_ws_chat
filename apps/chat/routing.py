from django.urls import path, include, re_path

from . import consumers

urlpatterns = [
    re_path(r"ws/chat/(?P<room_name>\w+)/$", consumers.ChatWebSocketConsumer.as_asgi()),
]