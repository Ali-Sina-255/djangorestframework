# Generated by Django 5.0.6 on 2024-07-08 12:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flightApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='passenger',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='flightApp.passenger'),
        ),
    ]
