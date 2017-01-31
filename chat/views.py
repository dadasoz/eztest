import logging
from django.shortcuts import render
from django.http import Http404
from django.db.models import Q

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from chat.models import Messages
from django.contrib.auth.models import User
from chat import serializers
from django.contrib.auth.decorators import login_required

@login_required
def index(request):

    users = User.objects.filter(~Q(id = request.user.id))

    context_data = {
                        "users":users,
                    }

    return render(request, "chat/chat.html", context_data)



class MessagesList(generics.ListAPIView):
    serializer_class = serializers.MessagesSerializer

    def get_queryset(self):
        post_data = self.request.GET
        receiver = post_data.get("receiver", None)

        if post_data.get("sender"):
            sender = User.objects.get(pk=post_data.get("sender", None))
        else:
            sender = User.objects.get(pk=self.request.user.id)

        receiver = User.objects.get(pk=receiver)

        queryset = Messages.objects.filter(Q(sender=sender, receiver=receiver) | Q(
            sender=receiver, receiver=sender)).order_by('timestamp')
        return queryset

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()

        serializer = serializers.MessagesSerializer(
            queryset, many=True)
        return Response(serializer.data)


class UsersList(generics.ListAPIView):
    serializer_class = serializers.UserSerializer

    def get_queryset(self):

        queryset = User.objects.filter(~Q(id = self.request.user.id))

        return queryset

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()

        serializer = serializers.UserSerializer(
            queryset, many=True)
        return Response(serializer.data)