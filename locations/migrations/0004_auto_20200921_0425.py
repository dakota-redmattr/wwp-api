# Generated by Django 3.1.1 on 2020-09-21 04:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0003_auto_20200921_0424'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='street_address1',
            new_name='street_address_1',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='street_address2',
            new_name='street_address_2',
        ),
    ]
