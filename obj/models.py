# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import uuid

class Obj(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=32)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=False)
    
    def getattr(self, name):
        return getattr(self, name)