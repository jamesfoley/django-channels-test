from testing.apps.site import routing

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    ),
})