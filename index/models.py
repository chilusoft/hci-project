from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    ski_id = models.CharField(max_length=255, null=True)

class Location(models.Model):
    name = models.CharField(max_length=255, null=True)

class MainRoute(models.Model):
    route_point = models.ForeignKey('SkiRoutePoints', on_delete=models.CASCADE)

class SkiRoutePoints(models.Model):
    material_icon = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

class DistanceCovered(models.Model):
    distance = models.FloatField(default=0)
    date_added = models.DateField(null=True)
    date_modified = models.DateField(auto_now=True)


class SnowCover(models.Model):
    inches = models.FloatField(default=0)
    date_added = models.DateField(null=True)
    date_modified = models.DateField(auto_now=True)


class DurationOfSki(models.Model):

    hrs = models.FloatField(default=0)
    date_added = models.DateField(null=True)


