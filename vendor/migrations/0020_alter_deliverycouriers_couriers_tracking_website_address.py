# Generated by Django 3.2.18 on 2023-04-14 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0019_deliverycouriers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliverycouriers',
            name='couriers_tracking_website_address',
            field=models.URLField(blank=True, null=True),
        ),
    ]
