# Generated by Django 2.1.4 on 2018-12-08 13:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='creationDate',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]
