from . import views
from django.urls import path

urlpatterns = [
    path('',views.account,name = "account"),
    path('logout_user',views.logout_user,name = "logout_user"),
]