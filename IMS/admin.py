from django.contrib import admin

# Register your models here.
from .models import Inventory
admin.site.register(Inventory)
from .models import Orders
from .models import Transaction
admin.site.register(Orders)
admin.site.register(Transaction)