# Generated by Django 2.1.5 on 2019-01-21 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic1app', '0011_merge_20190121_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='arrival',
            field=models.TimeField(max_length=30),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='departure',
            field=models.TimeField(max_length=30),
        ),
    ]
