# Generated by Django 2.2.6 on 2019-12-04 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0022_auto_20191203_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='condition',
            field=models.IntegerField(choices=[(4, 'Used - Not Working'), (1, 'Used - Like New'), (2, 'Used - Good'), (0, 'Brand New'), (3, 'Used - working')], default=4),
        ),
        migrations.AlterField(
            model_name='post',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
