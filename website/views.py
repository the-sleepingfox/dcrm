from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def home(request):
    # check to see if logingin
    if request.method == 'POST':
        username= request.POST['username']
        password= request.POST['password']
        # Authenticate
        user= authenticate(request, username=username, password= password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged")
            return redirect('home')
        else:
            messages.error(request, "Ther's an error, please try again")
            return redirect('home')
    else:
        return render(request, 'home.html', {})

def login_user(request):
    pass

def logout_user(request):
    pass