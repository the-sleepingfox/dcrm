from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record
# Create your views here.

def home(request):
    # imprting model Record and putting it in variable naem record
    records= Record.objects.all()
    # check to see if logingin
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
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
        return render(request, 'home.html', {'records':records})

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # User authentication and login
            username= form.cleaned_data['username']
            password= form.cleaned_data['password1']
            user= authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Successfully Registerd")
            return redirect('home')
    else:
        form= SignUpForm()
        return render(request, 'registeration-form.html', {'form':form})
    
    return render(request, 'registeration-form.html', {'form':form})

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, "Loggedout Succesfully!!")
    return redirect('home')

def create_record(request):
    form= AddRecordForm(request.POST or None)

    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_Record= form.save()
                messages.success(request, "Record Added Successfully...")
                return redirect('home')
        return render(request, 'create_record.html', {'form':form})
    else:
                messages.success(request, "You must have been Logged to add Record")
                return redirect('home')


def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record= Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, "You must be Logged in to view that page!")
        return redirect('home')

def update_record(request):
    pass

def delete_record(request, pk):
    if request.user.is_authenticated:
        customer_record= Record.objects.get(id=pk)
        messages.success(request, "Record deleted!")
        customer_record.delete()
        return redirect('home')
        
    else:
        messages.success(request, "You must be logged in first!")
        return redirect(request, 'home')