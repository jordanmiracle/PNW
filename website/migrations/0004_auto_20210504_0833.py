# Generated by Django 3.1.3 on 2021-05-04 08:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20210504_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 5, 4, 8, 33, 2, 792353)),
        ),
    ]
