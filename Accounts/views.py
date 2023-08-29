from django.shortcuts import render,redirect
from django.http import HttpResponse 
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.

def account(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username = username,password = password)
        if user is not None:
            login(request , user)
            return redirect("IMS/home")
        else:
            return HttpResponse("Not valid Username and Password")
    else:
        return render(request,'authentication/login.html',{})
    
def logout_user(request):
    logout(request)
    messages.success(request,("You are logged out"))
    return redirect('account')