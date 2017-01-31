from chat import consumers
from channels.routing import route

socket_routing = [
    route("websocket.connect", consumers.ws_connect),
    route("websocket.receive", consumers.ws_receive),
    route("websocket.disconnect", consumers.ws_disconnect),
]
