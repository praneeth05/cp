# Generated by Django 3.1.1 on 2020-12-13 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carpool', '0014_package'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Sedan',
            new_name='Carprice',
        ),
        migrations.DeleteModel(
            name='Compactsuv',
        ),
        migrations.DeleteModel(
            name='Hatchback',
        ),
        migrations.DeleteModel(
            name='Suv',
        ),
        migrations.AlterModelTable(
            name='carprice',
            table='Carprice',
        ),
    ]