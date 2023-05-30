from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #Auth
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in succesfully")
            return redirect('home')
        else:
            messages.success(request, "There was an error logging in")
            return redirect('home')
    else:
        return render(request, 'home.html',{})

def logout_user(request):
    logout(request)
    messages.success(request, "Logged out succesfully")
    return redirect('home')

