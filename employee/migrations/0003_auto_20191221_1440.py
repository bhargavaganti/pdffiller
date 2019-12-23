# Generated by Django 2.2.7 on 2019-12-21 14:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_individual_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='family',
            name='from_date',
            field=models.DateField(default=datetime.date(2020, 1, 1)),
        ),
        migrations.AddField(
            model_name='family',
            name='to_date',
            field=models.DateField(default=datetime.date(2020, 12, 31)),
        ),
        migrations.AddField(
            model_name='individual',
            name='from_date',
            field=models.DateField(default=datetime.date(2020, 1, 1)),
        ),
        migrations.AddField(
            model_name='individual',
            name='to_date',
            field=models.DateField(default=datetime.date(2020, 12, 31)),
        ),
        migrations.AlterField(
            model_name='family',
            name='Faadhar',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='family',
            name='Member_1_aadhar',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='individual',
            name='Faadhar',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]