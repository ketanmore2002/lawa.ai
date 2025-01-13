from django.urls import path
from .consumers import MyWebSocketConsumer

websocket_urlpatterns = [
    path('ws/chat/', MyWebSocketConsumer.as_asgi()),
]
