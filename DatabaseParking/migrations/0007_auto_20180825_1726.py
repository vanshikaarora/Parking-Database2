# Generated by Django 2.1 on 2018-08-25 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DatabaseParking', '0006_auto_20180825_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='amount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='total',
            field=models.IntegerField(),
        ),
    ]
