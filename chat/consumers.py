import re
import json
import logging
from channels import Group
from channels.sessions import channel_session
from channels.auth import channel_session_user_from_http

from chat.models import Messages
from django.contrib.auth.models import User
from chat.utils import getUserDict

log = logging.getLogger(__name__)


@channel_session_user_from_http
def ws_connect(message, room):
    log.debug("user=%s", room)
    message.reply_channel.send({"accept": True})
    user = User.objects.get(username=room)
    message.channel_session['user'] = getUserDict(user)
    #user = get_user(message)
    message.channel_session['room'] = room
    Group(room).add(message.reply_channel)

@channel_session
def ws_receive(message, room):
    data = None
    try:
        data = json.loads(message['text'])
        data.update({"sender": message.channel_session['user']})
    except ValueError:
        log.debug("ws message isn't json text=%s", data)
        return
    try:
        sender = User.objects.get(pk=data.get("sender").get("id"))
        receiver = User.objects.get(pk=data.get("receiver"))
        Messages.objects.create(
            sender=sender, receiver=receiver, message=data.get("message"))
    except Exception as ex:
        log.debug("error=%s", ex)
    try:
        Group(receiver.username,
              channel_layer=message.channel_layer).send({'text': json.dumps(data)})
    except:
        log.debug(
            "User has not joined yet, so he will receive this mssage offline.")


@channel_session
def ws_disconnect(message, room):
    try:
        Group(room,
              channel_layer=message.channel_layer).discard(message.reply_channel)
    except:
        pass
