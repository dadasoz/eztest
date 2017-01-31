from channels import include

channel_routing = [
    include("chat.routing.socket_routing",
            path=r"^/ws/chat/(?P<room>[^/]+)/$"),
]
