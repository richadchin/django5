# Generated by Django 3.2.18 on 2023-04-10 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0012_vendor_payout'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='payout_to_paypal',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='vendor',
            name='payout_to_stripe',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='vendor',
            name='payout_to_wallet',
            field=models.BooleanField(default=False),
        ),
    ]
