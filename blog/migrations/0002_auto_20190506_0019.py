# Generated by Django 2.2.1 on 2019-05-05 22:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 5, 22, 19, 10, 177298, tzinfo=utc)),
        ),
    ]
