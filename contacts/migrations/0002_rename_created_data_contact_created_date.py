# Generated by Django 4.1.4 on 2023-01-11 01:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("contacts", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="contact",
            old_name="created_data",
            new_name="created_date",
        ),
    ]