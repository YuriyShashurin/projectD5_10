# Generated by Django 3.1.3 on 2020-12-18 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0004_blog_small_decc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='small_decc',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
