from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Inventory
from .models import Orders
from .models import Transaction
from .forms import InventoryForm
from .forms import SellItemForm
from .forms import OrdersForm
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.

def index(request):
    
    inventory = Inventory.objects.all()
    return render(request,'index/index.html',{'inventory':inventory})

def home(request):
    items = Inventory.objects.all()

    total_profit = sum(item.profit_earned for item in items)
    total_items = items.count()

    highest_cost_item = items.order_by('-selling_price').first()
    highest_profit_item = items.order_by('-profit_earned').first()
    most_sold_item = items.order_by('-quantity_sold').first()

    out_of_stock_items = items.filter(quantity=0).count()

    highest_profit_earned_item = items.order_by('-profit_earned').first()

    context = {
        'total_profit': total_profit,
        'total_items': total_items,
        'highest_cost_item': highest_cost_item,
        'highest_profit_item': highest_profit_item,
        'most_sold_item': most_sold_item,
        'out_of_stock_items': out_of_stock_items,
        'highest_profit_earned_item': highest_profit_earned_item,
    }

    return render(request, 'home/index.html', context)    
    #return render(request,'home/index.html')

def itemList(request):
    items = Inventory.objects.all()
    return render(request, 'itemList/index.html', {'items': items})
    #return HttpResponse("This is ItemList Screen")

def sellItem(request,item_id):
    if request.method == 'POST':
        form = SellItemForm(request.POST)
        if form.is_valid():
            item = form.cleaned_data['item']
            quantity = form.cleaned_data['quantity']
            selling_price = form.cleaned_data['selling_price']

            try:
                inventory_item = Inventory.objects.get(id=item.id)
                if inventory_item.quantity >= quantity:
                    transaction = form.save(commit=False)
                    transaction.selling_price = selling_price
                    transaction.save()

                    # Update Inventory quantities
                    inventory_item.quantity -= quantity
                    inventory_item.quantity_sold += quantity
                    inventory_item.revenue += selling_price * quantity
                    inventory_item.profit_earned += (selling_price - inventory_item.cost) * quantity
                    inventory_item.save()

                    return redirect('itemList')  # Redirect to transaction list
                else:
                    form.add_error('quantity', "Insufficient quantity in stock")
            except Inventory.DoesNotExist:
                form.add_error('item', "Invalid item selected")
    else:
        form = SellItemForm()

    context = {'form': form}
    return render(request, 'sellItem/mm.html', context)

def createNewItem(request):
    #form = InventoryForm()
    if request.method == "POST":
        form = InventoryForm(request.POST)
        
        if form.is_valid():
            item = form.save(commit=False)
            if item.quantity >= item.quantity_sold:
                item.revenue = item.selling_price * item.quantity_sold
                item.profit_earned = item.revenue - (item.cost * item.quantity_sold)
                item.save()
            #form.save()
                return redirect('itemList')
            else:
                return HttpResponse("Quantity Sold Cannot be Greater Than Qunatity in Inventory")
    else:
        form = InventoryForm()
    context = {'form':form}
    return render(request,'createNewItem/mm.html',context)
    #return HttpResponse("This is createNewItem Screen")

def itemDetails(request,item_id):
    item = Inventory.objects.get(pk=item_id)
    return render(request,'itemDetails/index.html',{'item':item})

def ordersPlaced(request):
    return HttpResponse("This is ordersPlaced Screen")

def ordersReceived(request):
    return HttpResponse("This is ordersReceived Screen")

def ordersCancelled(request):
    return HttpResponse("This is ordersCancelled Screen")

def itemsSold(request):
    return HttpResponse("This is itemSold Screen")

def editItem(request, item_id):
    item = get_object_or_404(Inventory, pk=item_id)
    
    if request.method == 'POST':
        form = InventoryForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('itemList')  # Redirect to the item list page after editing
    else:
        form = InventoryForm(instance=item)

    context = {'form': form, 'item': item}
    return render(request, 'editItem/index.html', context)
    #return HttpResponse("This is editItem Screen")
    
def createOrders(request,item_id):
    moo = get_object_or_404(Inventory, pk=item_id)
    
    if request.method == 'POST':
        form = OrdersForm(request.POST,instance=moo)
        form.item = moo
        if form.is_valid():
            Orders = form.save(commit=False)
            if Orders.is_received:
                Orders.save()  # Save to Orders model
                item = Orders.item
                inventory_item = Inventory.objects.get(id=item.id)

                # Update Inventory quantities
                inventory_item.quantity += Orders.quantity
                inventory_item.save()

                return redirect('itemList')  # Redirect to order list
    else:
        form = OrdersForm()

    context = {'form': form}
    return render(request, 'createOrders/index.html', context)