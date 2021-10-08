# Generated by Django 3.2.8 on 2021-10-07 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='vehicles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=20)),
                ('vehicle_number', models.CharField(max_length=10)),
                ('documents', models.FileField(upload_to='')),
            ],
        ),
    ]
