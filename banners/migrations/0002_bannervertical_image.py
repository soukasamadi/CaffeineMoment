# Generated by Django 3.2.21 on 2023-10-09 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banners', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bannervertical',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='banners/'),
        ),
    ]