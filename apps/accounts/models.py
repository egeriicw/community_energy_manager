from django.db import models
from apps.weather.models import WeatherStation


# Create your models here.

class Address(models.Model):
    blocknum = models.CharField(max_length=10, blank=True, default='')
    line1 = models.CharField(max_length=100, blank=True, default='')
    line2 = models.CharField(max_length=100, blank=True, default='')
    line3 = models.CharField(max_length=100, blank=True, default='')
    unit = models.CharField(max_length=20, blank=True, default='')
    cityname = models.CharField(max_length=100, blank=True, default='')
    statename = models.CharField(max_length=100, blank=True, default='')
    stateabv = models.CharField(max_length=2, blank=True, default='')
    countryname = models.CharField(max_length=100, blank=True, default='')
    countryabv = models.CharField(max_length=3, blank=True, default='')
    zipcode = models.CharField(max_length=5, blank=True, default='')
    zipcode_ext = models.CharField(max_length=4, blank=True, default='')

    def __unicode__(self):
        return "%s %s %s; %s, %s %s" % (self.blocknum, self.line1, self.line2, self.cityname, self.stateabv, self.zipcode)

class Parcel(models.Model):
    id_number = models.CharField(max_length=12, blank=True, default='')
    land_area = models.CharField(max_length=10, blank=True, default='')
    owner = models.CharField(max_length=100, blank=True, default='')
    address = models.ForeignKey(Address, null=True)
    zoning = models.CharField(max_length=15, blank=True, default='')
    parcel_class = models.CharField(max_length=100, blank=True, default='')

class PropertyType(models.Model):
    property_type_name = models.CharField(max_length=100, default='')

    def __unicode__(self):
        return "%s" % (self.property_type_name)

class Property(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    
    property_type = models.ForeignKey(PropertyType, blank=True, null=True)

    # temporary address variables, will eventually replace with an Address model class
    # Address model class will link to other models

    address = models.ForeignKey(Address)

    fips = models.CharField(max_length=5, blank=True, default='')
    weather_station = models.ForeignKey(WeatherStation, blank=True, null=True)

    # Need to determine all sorts of census and demographic coding
    census = models.CharField(max_length=100, blank=True, default='')
    congressional_district = models.CharField(max_length=100, blank=True, default='')

    owner_name = models.CharField(max_length=100, blank=True, default='')
    census_tract = models.CharField(max_length=10, blank=True, default='')
    census_block = models.CharField(max_length=5, blank=True, default='')
    year_built = models.CharField(max_length=4, blank=True, default='')

    def __unicode__(self):
        return "%s" % (self.name)

class Account(models.Model):
    account_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=12)

    prop = models.ForeignKey(Property, null=True)

    def __unicode__(self):
        return "%s: %s" % (self.account_number, self.account_number)

    class Meta:
        ordering = ('account_number',)

class Meter(models.Model):
    meter_name = models.CharField(max_length=100)
    meter_number = models.CharField(max_length=15)

    account = models.ForeignKey(Account)

    def __unicode__(self):
        return "%s" % (self.meter_number)

class RecordType(models.Model):
    record_type = models.CharField(max_length=10)

class RecordUnits(models.Model):
    units = models.CharField(max_length=100)

class Record(models.Model):
    startdatetime = models.DateTimeField()
    enddatetime = models.DateTimeField()
    value = models.DecimalField(max_digits=10, decimal_places=2)
    record_type = models.ForeignKey(RecordType)
    record_units = models.ForeignKey(RecordUnits)

    meter = models.ForeignKey(Meter, null=True)

    def __unicode__(self):
        return "%s - %s: %s %s" % (self.startdatetime, self.enddatetime, self.value, self.record_units)
