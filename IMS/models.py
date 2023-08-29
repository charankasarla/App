from django.db import models
import uuid


class Inventory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    iin = models.CharField(max_length=100, default=uuid.uuid4)  # Item Identification Number
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    quantity_sold = models.PositiveIntegerField(default=0)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    profit_earned = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    revenue = models.DecimalField(max_digits=10, decimal_places=2,default=0)

    def __str__(self):
        return self.name

class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    item = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    orderdttm = models.DateTimeField()
    is_received = models.BooleanField(default=False)
    is_cancel = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    item = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    transactiondttm = models.DateTimeField()

    def __str__(self):
        return self.name
