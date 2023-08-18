from django import forms
from .models import Inventory
from .models import Orders, Transaction

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['name','cost','quantity', 'quantity_sold', 'selling_price']

class SellItemForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['item', 'quantity', 'selling_price','transactiondttm']

class OrdersForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['item','quantity', 'cost', 'orderdttm', 'is_received', 'is_cancel']