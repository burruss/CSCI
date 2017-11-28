from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
class Group(models.Model):
    name  = models.CharField(max_length=20)
    formed = models.IntegerField()
    def __str__(self):
        return self.name

class Artist(models.Model):
    artist = models.CharField(max_length=20)
    def __str__(self):
        return self.artist

class Member(models.Model):
    group = models.IntegerField()
    artist = models.IntegerField()
    def __int__(self):
        return self.group
