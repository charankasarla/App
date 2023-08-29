from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from .models import Inventory,Orders,Transaction
from .forms import InventoryForm,SellItemForm,OrdersForm
from django.utils import timezone
#from django.urls import reverse
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

def itemList(request):
    items = Inventory.objects.all()
    return render(request, 'itemList/index.html', {'items': items})

def sellItem(request,item_id):
    
    inventory_item = Inventory.objects.get(id=item_id)
    
    if request.method == 'POST':
        form = SellItemForm(request.POST)
        
        if form.is_valid():
            quantity = form.cleaned_data['quantity']

            if inventory_item.quantity >= quantity:
                selling_price = inventory_item.cost
                transaction = form.save(commit=False)
                transaction.name = inventory_item.name
                transaction.item = inventory_item
                transaction.selling_price = selling_price
                transaction.transactiondttm = timezone.now()
                transaction.save()

                # Update Inventory quantities
                inventory_item.quantity -= quantity
                inventory_item.quantity_sold += quantity
                inventory_item.revenue += selling_price * quantity
                inventory_item.profit_earned += (selling_price - inventory_item.cost) * quantity
                inventory_item.save()

                return redirect('itemList')  
            else:
                form.add_error('quantity', "Insufficient quantity in stock")
    else:
        initial_data = {
            'item': inventory_item,
            'selling_price': inventory_item.cost,  
        }
        form = SellItemForm(initial=initial_data)

    context = {'form': form}
    return render(request, 'sellItem/mm.html', context)
    
def createNewItem(request):
    if request.method == "POST":
        form = InventoryForm(request.POST)
        
        if form.is_valid():
            item = form.save(commit=False)
            if item.quantity >= item.quantity_sold:
                if item.selling_price>= item.cost:
                    item.revenue = item.selling_price * item.quantity_sold
                    item.profit_earned =  (item.selling_price - item.cost)* item.quantity_sold
                    item.save()
                    return redirect('itemList')
                else:
                    return HttpResponse("Selling Price should not be less than Cost Price")
                    
            else:
                return HttpResponse("Quantity Sold Cannot be Greater Than Qunatity in Inventory")
    else:
        form = InventoryForm()
    context = {'form':form}
    return render(request,'createNewItem/mm.html',context)

def itemDetails(request,item_id):
    item = Inventory.objects.get(id = item_id)
    context = {'item': item}
    return render(request,'itemDetails/index.html',context)

    
def ordersPlaced(item_id,quantity):
    order = Orders()
    item = Inventory.objects.get(id=item_id)
    order.item = item
    order.name = item.name
    order.quantity = quantity
    order.orderdttm = timezone.now()
    order.is_received = False
    order.is_cancel = False
    order.cost = item.cost * quantity
    order.save()
    return order.id


def ordersCancelled(request,item_id):
    orders_cancelled = Orders.objects.filter(item_id=item_id, is_cancel=True)

    context = {'orders': orders_cancelled,'context': "Cancelled"}
    return render(request, 'orders/index.html', context)

def itemsSold(request,item_id):
    transactions = Transaction.objects.filter(item_id=item_id)
    context = {'transactions': transactions}
    return render(request, 'itemsSold/index.html', context)

def editItem(request, item_id):
    item = Inventory.objects.get(pk = item_id)
    
    if request.method == 'POST':
        form = InventoryForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('itemList')
    else:
        form = InventoryForm(instance=item)

    context = {'form': form, 'item': item}
    return render(request, 'editItem/index.html', context)
    
def createOrders(request,item_id):
    
    item = Inventory.objects.get(id=item_id)

    if request.method == 'POST':
        form = OrdersForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            quantity = form.cleaned_data['quantity']
            order_id = ordersPlaced(item_id,quantity)
            return redirect('ordersDetails',order_id = order_id)
    else:
        initial_data = {
            'item': item,
            'name': item.name,  # Prepopulate item name
            'cost': item.cost,  # Prepopulate cost
        }
        form = OrdersForm(initial=initial_data)

    context = {'form': form}
    return render(request, 'createOrders/index.html', context)


    
def ordersReceived(request, item_id):
    orders_received = Orders.objects.filter(item_id=item_id, is_received=True)

    context = {'orders': orders_received,'context': "Received"}
    return render(request, 'orders/index.html', context)

def allOrders(request,item_id):
    orders = Orders.objects.filter(item_id=item_id)

    context = {'orders': orders,'context': ""}
    return render(request, 'orders/index.html', context)


def transactions(request,item_id):
    item = Inventory.objects.get(id=item_id)
    transactions = Transaction.objects.filter(item=item)
    
    context = {'transactions': transactions,'item':item}
    return render(request, 'transactions/index.html', context)

def confirmReceived(request, order_id):
    order = Orders.objects.get(id = order_id)
    order.is_received = True
    order.save()
    inventory_item = Inventory.objects.get(id=order.item.id)
    inventory_item.quantity += order.quantity
    inventory_item.save()
    return redirect('itemList')

def confirmCanceled(request, order_id):
    order = Orders.objects.get(id=order_id)
    order.is_cancel = True
    order.save()
    return redirect('itemList')

def ordersDetails(request,order_id):
    order = Orders.objects.get(id = order_id)
    context = {'order':order}
    return render(request, 'ordersPlaced/index.html', context)