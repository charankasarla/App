# Generated by Django 4.2.4 on 2023-08-18 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('iin', models.CharField(max_length=20, unique=True)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField()),
                ('quantity_sold', models.PositiveIntegerField()),
                ('selling_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('profit_earned', models.DecimalField(decimal_places=2, max_digits=10)),
                ('revenue', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.PositiveIntegerField()),
                ('selling_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('transactiondttm', models.DateTimeField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IMS.inventory')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.PositiveIntegerField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('orderdttm', models.DateTimeField()),
                ('is_received', models.BooleanField(default=False)),
                ('is_cancel', models.BooleanField(default=False)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IMS.inventory')),
            ],
        ),
    ]
