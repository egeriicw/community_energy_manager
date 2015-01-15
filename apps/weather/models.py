from django.db import models

# Create your models here.

class WeatherStation(models.Model):
    # "USAF","WBAN","STATION NAME","CTRY","STATE","LAT","LON","ELEV(M)","BEGIN","END"
    # "724050","13743","RONALD REAGAN WASHINGTON NATL AP","US","VA","+38.848","-077.034","+0003.1","20050101","20140403"

    usaf = models.CharField(max_length=6, default='')
    wban = models.CharField(max_length=5, default='99999')
    station_name = models.CharField(max_length=60, default='')
    country = models.CharField(max_length=2, default='')
    state = models.CharField(max_length=2, default='')
    lat = models.CharField(max_length=7, default='')
    lon = models.CharField(max_length=8, default='')
    elev = models.CharField(max_length=7, default='')
    begin_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)

    def __unicode__(self):
        return "%s" % (self.station_name)

class WeatherRecord(models.Model):

    measure_date = models.DateField(auto_now=False, auto_now_add=False)
    avg_temp = models.FloatField()
    avg_temp_count = models.IntegerField()
    
    avg_dewp_temp = models.FloatField()
    avg_dewp_temp_count = models.IntegerField()

    # Average sea level pressure for the day (in millibars)

    avg_slp = models.FloatField()
    avg_slp_count = models.IntegerField()
 
    # Average standard pressure for the day (in millibars)

    avg_stp = models.FloatField()
    avg_stp_count = models.IntegerField()

    weather_station = models.ForeignKey(WeatherStation, blank=True, null=True)

    def __unicode__(self):
        return "%s" % (self.measure_date)
