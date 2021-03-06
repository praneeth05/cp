# Generated by Django 3.1.1 on 2020-12-10 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carpool', '0013_auto_20201210_2257'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.EmailField(max_length=100)),
                ('username', models.EmailField(max_length=125)),
                ('regno', models.CharField(max_length=25)),
                ('address', models.CharField(max_length=225)),
                ('phone', models.CharField(max_length=25)),
                ('date', models.CharField(max_length=25)),
                ('time', models.CharField(max_length=25)),
                ('cartype', models.CharField(max_length=25)),
                ('package', models.CharField(max_length=225)),
            ],
            options={
                'db_table': 'Package',
            },
        ),
    ]
