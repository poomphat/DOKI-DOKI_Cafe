# Generated by Django 3.0.5 on 2020-04-16 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20200415_1825'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='queue',
        ),
        migrations.DeleteModel(
            name='Queue_info',
        ),
    ]
