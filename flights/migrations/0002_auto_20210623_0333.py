# Generated by Django 3.2.4 on 2021-06-23 03:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='arrival_city_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flight_arrival', to='flights.city'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='arrival_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='flight',
            name='arrival_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='flight',
            name='departure_city_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flight_departure', to='flights.city'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='departure_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='flight',
            name='departure_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='flight',
            name='duration',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='seat',
            name='name',
            field=models.CharField(max_length=45),
        ),
    ]
