from django.contrib import admin

# Register your models here.
from .models import User, MainRoute, SkiRoutePoints, DistanceCovered, SnowCover, Location, DurationOfSki

admin.site.register(User)
admin.site.register(MainRoute)
admin.site.register(SkiRoutePoints)
admin.site.register(DistanceCovered)
admin.site.register(SnowCover)
admin.site.register(Location)
admin.site.register(DurationOfSki)
