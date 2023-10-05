# Generated by Django 3.2.21 on 2023-10-05 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BannerVertical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('description', models.TextField()),
                ('image_small', models.ImageField(blank=True, null=True, upload_to='banners/')),
                ('featured', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Vertical Banner',
            },
        ),
    ]
