from django import forms 
from .models import Orders, Transaction,Inventory

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['name','cost','quantity','selling_price']

class SellItemForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['item', 'quantity']

class OrdersForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['name', 'item', 'quantity', 'cost']