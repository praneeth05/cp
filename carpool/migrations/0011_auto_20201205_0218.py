# Generated by Django 3.1.1 on 2020-12-04 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carpool', '0010_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='address',
            field=models.CharField(default=122, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='cartype',
            field=models.CharField(default=12, max_length=25),
            preserve_default=False,
        ),
    ]