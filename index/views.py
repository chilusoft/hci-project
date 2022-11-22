from django.db.models import Sum
from django.shortcuts import render
from datetime import datetime, timedelta

from .models import DistanceCovered, SnowCover, DurationOfSki, MainRoute


# Create your views here.

def index(request):

    # past Seven days stats
    #   Distance
    distance_for_previous_week = DistanceCovered.objects.filter(date_added__range=[datetime.now().date() - timedelta(days=7), datetime.now().date()])
    distance_for_previous_week = distance_for_previous_week.aggregate(Sum('distance'))['distance__sum']
    #   Duration
    duration_for_previous_week = DurationOfSki.objects.filter(
        date_added__range=[datetime.now().date() - timedelta(days=7), datetime.now().date()])
    duration_for_previous_week = duration_for_previous_week.aggregate(Sum('hrs'))['hrs__sum']

    #all time stats
    all_time_distance_sum = DistanceCovered.objects.filter(date_added__lte=datetime.now().date()).aggregate(Sum('distance'))
    all_time_duration_sum = DurationOfSki.objects.filter(date_added__lte=datetime.now().date()).aggregate(Sum('hrs'))
    total_distance = all_time_distance_sum['distance__sum']
    total_duration = all_time_duration_sum['hrs__sum']
    distance_pack = []
    duration_pack = []
    snow_cover_pack = []
    week_pack = []
    for x in range(7):
        week_pack_el = datetime.now() - timedelta(days=x)
        week_pack.append(week_pack_el)

    distance_query_set = DistanceCovered.objects.filter(date_added__lte=datetime.now())
    snow_cover_query_set = SnowCover.objects.filter(date_added__lte=datetime.now())
    ski_duration_query_set = DurationOfSki.objects.filter(date_added__lte=datetime.now())
    for record in distance_query_set:
        distance_pack.append(record.distance)

    for record in ski_duration_query_set:
        duration_pack.append(record.hrs)

    for record in snow_cover_query_set:
        snow_cover_pack.append(record.inches)

    skiis = MainRoute.objects.all()
    num_skiis_count = MainRoute.objects.all().count()


    ctx = {
        'week_pack': week_pack,
        'distance_pack': distance_pack,
        'snow_cover_pack': snow_cover_pack,
        'duration_pack': duration_pack,
        'total_distance': total_distance,
        'distance_for_previous_week': distance_for_previous_week,
        'total_duration': total_duration,
        'duration_for_previous_week':  duration_for_previous_week,
        'skiis': skiis,
        'num_skiis_count': num_skiis_count

    }

    return render(request, 'index/index.html', ctx)


def data(request):
    return render(request, 'index/data.html')
