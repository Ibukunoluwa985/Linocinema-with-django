# Generated by Django 3.1.8 on 2021-06-25 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvshows', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tvshows',
            name='year',
            field=models.PositiveIntegerField(),
        ),
    ]
