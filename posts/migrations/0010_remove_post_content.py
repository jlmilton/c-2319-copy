# Generated by Django 2.2.6 on 2019-11-11 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20191110_2349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
    ]