import os
from django.core.asgi import get_asgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Tiktactoe.settings')
from channels.routing import ProtocolTypeRouter,URLRouter
from main import routing
application =ProtocolTypeRouter(
    {
        'http': get_asgi_application(),
        'websocket':URLRouter(routing.websocketurlpattern)
    }
)