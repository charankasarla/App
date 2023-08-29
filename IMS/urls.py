from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name = "index"),
    path('home/',views.home, name = "home"),
    path('itemList/',views.itemList, name = "itemList"),
    path('sellItem/<int:item_id>/',views.sellItem, name = "sellItem"),
    path('createNewItem/',views.createNewItem, name = "createNewItem"),
    path('itemDetails/<int:item_id>/',views.itemDetails, name = "itemDetails"),
    path('ordersPlaced/<int:item_id>/<int:quantity>',views.ordersPlaced, name = "ordersPlaced"),
    path('ordersDetails/<int:order_id>/',views.ordersDetails, name = "ordersDetails"),
    path('ordersCancelled/<int:item_id>/',views.ordersCancelled, name = "ordersCancelled"),
    path('ordersReceived/<int:item_id>/',views.ordersReceived, name = "ordersReceived"),
    path('itemsSold/<int:item_id>/',views.itemsSold, name = "itemsSold"),
    path('editItem/<int:item_id>/',views.editItem, name = "editItem"),
    path('createOrders/<int:item_id>/',views.createOrders, name = "createOrders"),
    path('transactions/<int:item_id>/', views.transactions, name='transactions'),
    path('confirmReceived/<int:order_id>/', views.confirmReceived, name='confirmReceived'),
    path('confirmCanceled/<int:order_id>/', views.confirmCanceled, name='confirmCanceled'),\
    path('allOrders/<int:item_id>/', views.allOrders, name='allOrders'),
]