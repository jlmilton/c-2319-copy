# Generated by Django 3.0.5 on 2020-04-15 22:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0006_auto_20200415_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='state',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='street',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='zip',
            field=models.IntegerField(blank=True, default='', null=True, validators=[django.core.validators.MaxValueValidator(100000)]),
        ),
    ]
