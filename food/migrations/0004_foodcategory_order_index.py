# Generated by Django 3.1.1 on 2020-10-31 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_auto_20200921_0332'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodcategory',
            name='order_index',
            field=models.IntegerField(null=True),
        ),
    ]