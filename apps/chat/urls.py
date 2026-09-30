from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.chatView, name="chat_page"),
    path("login/", views.login_view, name="login"),
    path("room/", views.chat_page, name="chat_room"),
    path("<str:room_name>/", views.chat_room, name="room")
]