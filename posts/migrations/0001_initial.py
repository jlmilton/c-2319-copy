# Generated by Django 3.0.3 on 2020-02-27 01:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField(null=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('category', models.IntegerField(choices=[(0, 'Electronic'), (1, 'Furniture'), (2, 'Major Appliance'), (3, 'Kitchen'), (4, 'Books'), (5, 'Motors')], default=0)),
                ('cover', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('condition', models.IntegerField(choices=[(0, 'Brand New'), (2, 'Used - Good'), (1, 'Used - Like New'), (3, 'Used - working'), (4, 'Used - Not Working')], default=4)),
                ('price', models.FloatField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]