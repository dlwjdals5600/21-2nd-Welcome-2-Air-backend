# Generated by Django 3.2.4 on 2021-06-23 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_auto_20210623_0333'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flight',
            old_name='arrival_date',
            new_name='arrival_datetime',
        ),
        migrations.RenameField(
            model_name='flight',
            old_name='arrival_time',
            new_name='departure_datetime',
        ),
        migrations.RenameField(
            model_name='flightseat',
            old_name='seat_id',
            new_name='seat',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='arrival_city_id',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='departure_city_id',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='departure_date',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='departure_time',
        ),
        migrations.RemoveField(
            model_name='flightseat',
            name='flight_id',
        ),
        migrations.AddField(
            model_name='flight',
            name='arrival_city',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='flight_arrival_city', to='flights.city'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flight',
            name='departure_city',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='flight_departure_city', to='flights.city'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flightseat',
            name='flight',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='flight_seat_flight', to='flights.flight'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='flight',
            name='duration',
            field=models.TimeField(),
        ),
    ]
