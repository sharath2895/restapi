# Generated by Django 3.2.16 on 2023-01-13 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='venue_id',
            new_name='venue',
        ),
    ]
