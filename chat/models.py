from __future__ import unicode_literals

from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Messages(models.Model):
    sender = models.ForeignKey(User, related_name='message_sender', null=True)
    receiver = models.ForeignKey(User, related_name='message_receiver', null=True)
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now,)
    is_seen = models.BooleanField(default=False,)
    is_seen_time = models.DateTimeField(default=None, null=True, blank=True)

    def __unicode__(self):
        return '[{timestamp}] {user}: {message}'.format(**self.as_dict())

    @property
    def formatted_timestamp(self):
        return self.timestamp.strftime('%b %-d %-I:%M %p')

    def as_dict(self):
        return {'message': self.message,
                'timestamp': self.formatted_timestamp,
                'sender': self.sender,
                'receiver': self.receiver,
                'is_seen': self.is_seen,
                'is_seen_time': self.is_seen_time, }
