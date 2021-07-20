# Generated by Django 3.1.8 on 2021-07-18 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movies',
            name='slider_image_link',
        ),
        migrations.AddField(
            model_name='movies',
            name='slider_image',
            field=models.ImageField(default='../static/images/no-image.png', upload_to='slider_img/movies'),
        ),
    ]