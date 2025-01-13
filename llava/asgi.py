"""
ASGI config for llava project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

# import os

# from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'llava.settings')

# application = get_asgi_application()


import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from rag_app.routing import websocket_urlpatterns  # Import your app's WebSocket routes

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'llava.settings')  # Project settings module

application = ProtocolTypeRouter({
    'http': get_asgi_application(),  # Handles HTTP requests
    'websocket': AuthMiddlewareStack(  # Handles WebSocket requests
        URLRouter(
            websocket_urlpatterns  # WebSocket routes from the app
        )
    ),
})



