# Generated by Django 4.2.4 on 2023-08-27 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IMS', '0005_alter_inventory_iin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='profit_earned',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='quantity_sold',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='revenue',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
