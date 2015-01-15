from django.contrib import admin
from apps.weather.models import WeatherStation
from apps.weather.models import WeatherRecord


# Register your models here.
admin.site.register(WeatherStation)
admin.site.register(WeatherRecord)

