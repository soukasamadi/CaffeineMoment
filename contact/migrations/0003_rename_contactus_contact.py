# Generated by Django 3.2.21 on 2023-10-09 13:58

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("contact", "0002_alter_contactus_options"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="contactUs",
            new_name="Contact",
        ),
    ]
