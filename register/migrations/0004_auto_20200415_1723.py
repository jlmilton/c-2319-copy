# Generated by Django 3.0.5 on 2020-04-15 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_auto_20200415_1647'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='location',
            new_name='state',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='street',
            field=models.CharField(blank=True, default=0, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='zip',
            field=models.IntegerField(blank=True, default=0, max_length=30, null=True),
        ),
    ]