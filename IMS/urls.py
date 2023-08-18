from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name = "index"),
    path('home/',views.home, name = "home"),
    path('itemList/',views.itemList, name = "itemList"),
    path('sellItem/<int:item_id>/',views.sellItem, name = "sellItem"),
    path('createNewItem/',views.createNewItem, name = "createNewItem"),
    path('itemDetails/<int:item_id>/',views.itemDetails, name = "itemDetails"),
    path('ordersPlaced/',views.ordersPlaced, name = "ordersPlaced"),
    path('ordersCancelled/',views.ordersCancelled, name = "ordersCancelled"),
    path('ordersReceived/',views.ordersReceived, name = "ordersReceived"),
    path('itemsSold/',views.itemsSold, name = "itemsSold"),
    path('editItem/<int:item_id>/',views.editItem, name = "editItem"),
    path('createOrders/<int:item_id>/',views.createOrders, name = "createOrders"),
]