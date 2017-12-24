# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class webinar(models.Model):
    name = models.CharField(max_length=15)
    email = models.TextField(max_length=20)
    phone = models.IntegerField()
    city = models.CharField(max_length=15)
    profession = models.CharField(max_length=15)
   
def _str_(self):
    return self.name