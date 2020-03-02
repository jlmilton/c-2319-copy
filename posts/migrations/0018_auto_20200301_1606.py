# Generated by Django 3.0.3 on 2020-03-01 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0017_auto_20200301_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='condition',
            field=models.IntegerField(choices=[(2, 'Used - Good'), (4, 'Used - Not Working'), (1, 'Used - Like New'), (0, 'Brand New'), (3, 'Used - working')], default=4),
        ),
    ]