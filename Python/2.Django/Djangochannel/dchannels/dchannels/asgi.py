"""
ASGI config for dchannels project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

# import os

# from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dchannels.settings')

# application = get_asgi_application()


# application = ProtocolTypeRouter({
# "http": get_asgi_application(),
#   "websocket": AuthMiddlewareStack(
#         URLRouter(
#             pratice.routing.websocket_urlpatterns
#             # liveCalculator.routing.websocket_urlpatterns
#         )
#     ),
# })



import os
  
import django
from channels.http import AsgiHandler
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import liveCalculator.routing
import pratice.routing
import pratice1.routing
import chatapp.routing
  
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sampleProject.settings')
django.setup()
  
application = ProtocolTypeRouter({
"http": get_asgi_application(),
  "websocket": URLRouter(chatapp.routing.websocket_urlpatterns)
})