# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('measure_date', models.DateField()),
                ('avg_temp', models.FloatField()),
                ('avg_temp_count', models.IntegerField()),
                ('avg_dewp_temp', models.FloatField()),
                ('avg_dewp_temp_count', models.IntegerField()),
                ('avg_slp', models.FloatField()),
                ('avg_slp_count', models.IntegerField()),
                ('avg_stp', models.FloatField()),
                ('avg_stp_count', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WeatherStation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('usaf', models.CharField(default=b'', max_length=6)),
                ('wban', models.CharField(default=b'99999', max_length=5)),
                ('station_name', models.CharField(default=b'', max_length=60)),
                ('country', models.CharField(default=b'', max_length=2)),
                ('state', models.CharField(default=b'', max_length=2)),
                ('lat', models.CharField(default=b'', max_length=7)),
                ('lon', models.CharField(default=b'', max_length=8)),
                ('elev', models.CharField(default=b'', max_length=7)),
                ('begin_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='weatherrecord',
            name='weather_station',
            field=models.ForeignKey(blank=True, to='weather.WeatherStation', null=True),
            preserve_default=True,
        ),
    ]
