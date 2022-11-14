from django.urls import path
from . import consumer
websocketurlpattern=[
    path('ws/',consumer.MySyncConsumer.as_asgi())
]