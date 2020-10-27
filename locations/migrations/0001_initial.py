# Generated by Django 3.1.1 on 2020-09-21 03:32

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LocationHours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monday_open', models.TimeField()),
                ('monday_close', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('street_address1', models.CharField(max_length=150)),
                ('street_address2', models.CharField(max_length=150, null=True)),
                ('picture', models.ImageField(upload_to='')),
                ('slug', models.SlugField()),
                ('phone', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('hours', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.locationhours')),
            ],
        ),
    ]
