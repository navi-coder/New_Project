# Generated by Django 3.2.8 on 2021-10-07 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carbooking', '0006_alter_driver_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='number',
            field=models.IntegerField(max_length=20),
        ),
    ]