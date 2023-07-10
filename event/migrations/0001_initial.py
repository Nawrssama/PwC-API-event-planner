# Generated by Django 4.2.3 on 2023-07-10 01:49

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('rank', models.IntegerField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('location_x', models.FloatField(max_length=255)),
                ('location_y', models.FloatField(max_length=255)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='event.event')),
                ('humidity', models.IntegerField(max_length=100)),
                ('temperature', models.IntegerField(max_length=100)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airport_code', models.CharField(max_length=100)),
                ('flight_number', models.CharField(max_length=100)),
                ('departure_time', models.DateTimeField()),
                ('arrival_time', models.DateTimeField()),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.event')),
            ],
        ),
    ]
