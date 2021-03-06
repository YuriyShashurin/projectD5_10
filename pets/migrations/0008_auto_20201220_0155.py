# Generated by Django 3.1.3 on 2020-12-19 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0007_auto_20201220_0153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='type',
            field=models.CharField(choices=[('Коты', 'Коты'), ('Собаки', 'Собаки'), ('Попугаи', 'Попугаи')], max_length=30, verbose_name='Тип животного'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='sex',
            field=models.CharField(choices=[('Мальчик', 'Мальчик'), ('Девочка', 'Девочка')], max_length=10, verbose_name='Пол питомца'),
        ),
    ]
