# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('account_name', models.CharField(max_length=100)),
                ('account_number', models.CharField(max_length=12)),
            ],
            options={
                'ordering': ('account_number',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('blocknum', models.CharField(default=b'', max_length=10, blank=True)),
                ('line1', models.CharField(default=b'', max_length=100, blank=True)),
                ('line2', models.CharField(default=b'', max_length=100, blank=True)),
                ('line3', models.CharField(default=b'', max_length=100, blank=True)),
                ('unit', models.CharField(default=b'', max_length=20, blank=True)),
                ('cityname', models.CharField(default=b'', max_length=100, blank=True)),
                ('statename', models.CharField(default=b'', max_length=100, blank=True)),
                ('stateabv', models.CharField(default=b'', max_length=2, blank=True)),
                ('countryname', models.CharField(default=b'', max_length=100, blank=True)),
                ('countryabv', models.CharField(default=b'', max_length=3, blank=True)),
                ('zipcode', models.CharField(default=b'', max_length=5, blank=True)),
                ('zipcode_ext', models.CharField(default=b'', max_length=4, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Meter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('meter_name', models.CharField(max_length=100)),
                ('meter_number', models.CharField(max_length=15)),
                ('account', models.ForeignKey(to='accounts.Account')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Parcel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_number', models.CharField(default=b'', max_length=12, blank=True)),
                ('land_area', models.CharField(default=b'', max_length=10, blank=True)),
                ('owner', models.CharField(default=b'', max_length=100, blank=True)),
                ('zoning', models.CharField(default=b'', max_length=15, blank=True)),
                ('parcel_class', models.CharField(default=b'', max_length=100, blank=True)),
                ('address', models.ForeignKey(to='accounts.Address', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=100, blank=True)),
                ('fips', models.CharField(default=b'', max_length=5, blank=True)),
                ('census', models.CharField(default=b'', max_length=100, blank=True)),
                ('congressional_district', models.CharField(default=b'', max_length=100, blank=True)),
                ('owner_name', models.CharField(default=b'', max_length=100, blank=True)),
                ('census_tract', models.CharField(default=b'', max_length=10, blank=True)),
                ('census_block', models.CharField(default=b'', max_length=5, blank=True)),
                ('year_built', models.CharField(default=b'', max_length=4, blank=True)),
                ('address', models.ForeignKey(to='accounts.Address')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PropertyType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('property_type_name', models.CharField(default=b'', max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('startdatetime', models.DateTimeField()),
                ('enddatetime', models.DateTimeField()),
                ('value', models.DecimalField(max_digits=10, decimal_places=2)),
                ('meter', models.ForeignKey(to='accounts.Meter', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RecordType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('record_type', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RecordUnits',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('units', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='record',
            name='record_type',
            field=models.ForeignKey(to='accounts.RecordType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='record',
            name='record_units',
            field=models.ForeignKey(to='accounts.RecordUnits'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='property',
            name='property_type',
            field=models.ForeignKey(blank=True, to='accounts.PropertyType', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='property',
            name='weather_station',
            field=models.ForeignKey(blank=True, to='weather.WeatherStation', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='account',
            name='prop',
            field=models.ForeignKey(to='accounts.Property', null=True),
            preserve_default=True,
        ),
    ]
