# Generated by Django 3.1.1 on 2020-12-04 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carpool', '0008_auto_20201026_2343'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(default=8197488955, max_length=25),
            preserve_default=False,
        ),
    ]
