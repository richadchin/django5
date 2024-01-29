# Generated by Django 3.2.18 on 2023-05-06 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0079_cartorderitem_original_grand_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartorder',
            name='original_total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
    ]
