# Generated by Django 3.0.5 on 2020-04-22 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_drink_info_how_to_make'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='picture',
            field=models.ImageField(blank=True, default='customer/default.png', null=True, upload_to='customer/'),
        ),
    ]
