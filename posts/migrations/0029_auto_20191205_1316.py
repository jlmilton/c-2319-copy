# Generated by Django 2.2.7 on 2019-12-05 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0028_auto_20191204_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='condition',
            field=models.IntegerField(choices=[(0, 'Brand New'), (3, 'Used - working'), (1, 'Used - Like New'), (4, 'Used - Not Working'), (2, 'Used - Good')], default=4),
        ),
    ]