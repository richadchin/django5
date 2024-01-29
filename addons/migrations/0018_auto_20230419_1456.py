# Generated by Django 3.2.18 on 2023-04-19 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addons', '0017_auto_20230419_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='supportcontactinformation',
            name='closing_time',
            field=models.CharField(blank=True, default='05 PM', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='supportcontactinformation',
            name='open_time',
            field=models.CharField(blank=True, default='08 AM', max_length=100, null=True),
        ),
    ]
