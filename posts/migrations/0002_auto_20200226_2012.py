# Generated by Django 3.0.3 on 2020-02-27 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
        migrations.AlterField(
            model_name='post',
            name='condition',
            field=models.IntegerField(choices=[(2, 'Used - Good'), (3, 'Used - working'), (1, 'Used - Like New'), (0, 'Brand New'), (4, 'Used - Not Working')], default=4),
        ),
    ]