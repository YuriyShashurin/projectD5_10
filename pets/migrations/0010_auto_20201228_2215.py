# Generated by Django 3.1.3 on 2020-12-28 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0009_auto_20201228_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Название статьи'),
        ),
    ]
