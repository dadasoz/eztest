from rest_framework import serializers
from chat.models import Messages
from django.contrib.auth.models import User

class MessagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Messages
        fields = (
            'pk', 'message', 'sender', 'receiver', 'timestamp', 'sender','is_seen','is_seen_time', )


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'pk', 'username', )