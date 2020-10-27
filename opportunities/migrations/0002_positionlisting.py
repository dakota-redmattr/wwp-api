# Generated by Django 3.1.1 on 2020-09-21 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0007_auto_20200921_0539'),
        ('opportunities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PositionListing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('filled', models.BooleanField(default=False)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location', to='locations.location')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='position', to='opportunities.positiontype')),
            ],
        ),
    ]
