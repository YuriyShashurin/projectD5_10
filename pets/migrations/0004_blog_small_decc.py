# Generated by Django 3.1.3 on 2020-12-18 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0003_auto_20201218_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='small_decc',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
