# Generated by Django 4.0.3 on 2022-03-22 05:39

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(default='room_images/default.jpg', upload_to='room_image')),
                ('room_no', models.CharField(max_length=10)),
                ('room_type', models.CharField(choices=[('single-bed', 'single-bed'), ('duble-bed', 'duble-bed'), ('family-bed', 'family-bed')], max_length=10)),
                ('price', models.IntegerField()),
                ('is_available', models.BooleanField(default=True)),
                ('day', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='BookingDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('no_of_guests', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('booked_on', models.DateTimeField(auto_now=True)),
                ('room', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='room.room')),
                ('user', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
