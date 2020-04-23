# Generated by Django 3.0.5 on 2020-04-17 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_auto_20200416_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='drink_info',
            name='useable_status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='fruit',
            name='useable_status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='option',
            name='useable_status',
            field=models.BooleanField(default=True),
        ),
    ]