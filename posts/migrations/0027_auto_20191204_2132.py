# Generated by Django 2.2.6 on 2019-12-05 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0026_auto_20191204_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='condition',
            field=models.IntegerField(choices=[(3, 'Used - working'), (4, 'Used - Not Working'), (2, 'Used - Good'), (1, 'Used - Like New'), (0, 'Brand New')], default=4),
        ),
    ]
