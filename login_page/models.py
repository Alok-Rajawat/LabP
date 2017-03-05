from __future__ import unicode_literals

from django.db import models

# Create your models here.
class user(models.Model):
    uname = models.CharField(max_length=30)
    passw = models.CharField(max_length=10)
