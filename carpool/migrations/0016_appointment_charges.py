# Generated by Django 3.1.1 on 2020-12-13 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carpool', '0015_auto_20201213_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='charges',
            field=models.CharField(default=250, max_length=25),
            preserve_default=False,
        ),
    ]
