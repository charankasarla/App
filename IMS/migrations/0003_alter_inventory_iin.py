# Generated by Django 4.2.4 on 2023-08-21 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IMS', '0002_alter_inventory_iin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='iin',
            field=models.CharField(max_length=100),
        ),
    ]
