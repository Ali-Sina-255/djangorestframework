# Generated by Django 5.0.6 on 2024-07-04 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='books',
            options={'verbose_name': 'book', 'verbose_name_plural': 'books'},
        ),
    ]