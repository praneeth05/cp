# Generated by Django 3.1.1 on 2020-12-13 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carpool', '0020_auto_20201213_2108'),
    ]

    operations = [
        migrations.RenameField(
            model_name='package',
            old_name='username',
            new_name='name',
        ),
        migrations.AddField(
            model_name='package',
            name='charges',
            field=models.CharField(default=33, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='package',
            name='msg',
            field=models.CharField(default=55, max_length=225),
            preserve_default=False,
        ),
    ]
