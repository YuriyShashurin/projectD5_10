# Generated by Django 3.1.3 on 2020-12-18 19:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Дата опубликования')),
                ('date', models.DateTimeField(default=datetime.date(2020, 12, 18), verbose_name='Дата опубликования')),
                ('blogpost', models.TextField()),
            ],
        ),
    ]
