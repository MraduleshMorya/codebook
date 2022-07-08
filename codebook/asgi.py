"""
ASGI config for codebook project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""
##  predefined
# import os
#
# from django.core.asgi import get_asgi_application
#
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codebook.settings')
#
# application = get_asgi_application()

## custom added
# mysite/asgi.py
import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from channels.sessions import SessionMiddlewareStack

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codebook.settings')
# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
django_asgi_app = get_asgi_application()

import asgi_channel_test.routing

application = ProtocolTypeRouter({
  "http": django_asgi_app,
  "websocket": AllowedHostsOriginValidator(
        SessionMiddlewareStack(
            URLRouter(
                asgi_channel_test.routing.websocket_urlpatterns
            )
        )
    ),
})