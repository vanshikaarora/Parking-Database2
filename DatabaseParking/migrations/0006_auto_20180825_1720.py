# Generated by Django 2.1 on 2018-08-25 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DatabaseParking', '0005_auto_20180825_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='amount',
            field=models.IntegerField(default=1, max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='total',
            field=models.IntegerField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]