# Generated by Django 3.2.21 on 2023-10-02 19:46

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="has_sizes",
        ),
    ]
