# Generated by Django 3.1.1 on 2020-12-13 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carpool', '0019_auto_20201213_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='Washtime',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='dettime',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='package',
            name='Washtime',
            field=models.CharField(max_length=25),
        ),
    ]
