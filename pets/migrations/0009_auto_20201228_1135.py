# Generated by Django 3.1.3 on 2020-12-28 08:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0008_auto_20201220_0155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='date_enter',
            field=models.DateField(default=datetime.date(2020, 12, 28), verbose_name='Дата поступления'),
        ),
    ]
