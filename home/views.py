from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request,"index.html")

def loginUser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        passwd=request.POST.get('pass')
        user=authenticate(username=username,password=passwd)
        if user:
            login(request,user)
            return redirect('/')
        
    return render(request,"login.html")

def signup(request):
    return render(request,"signup.html")

def logoutUser(request):
    logout(request)
    return redirect('/login')
