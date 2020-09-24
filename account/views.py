from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def Home(request):
    return render(request, 'account/home.html',{'name': 'Home page'})


def Signup(request):
    if request.method == 'POST':
        if request.POST['userPassword'] == request.POST['userConfirmPassword']:
            try:
                user = User.objects.get(username = request.POST['username'])
                return render(request, 'account/signup.html',{'name': 'Signup page', 'error':'User name has already been registered!'})
                print(user)
            except ObjectDoesNotExist:
                user = User.objects.create_user(request.POST['username'], password = request.POST['userPassword'])
                auth.login(request, user)
                return redirect('homepage')
        else:
            return render(request, 'account/signup.html',{'name': 'Signup page', 'error':'Password and confirm password donot match!'})
    else:
        return render(request, 'account/signup.html',{'name': 'Signup page'})
    

def Login(request):
    if request.method == 'POST':
        user = auth.authenticate(username = request.POST['username'], password = request.POST['userPassword'])
        if user is not None:
            auth.login(request, user)
            return redirect('homepage')
        else:
            return render(request, 'account/login.html',{'name': 'Login page', 'error':"Your user name and password don't match"})
    else:
        return render(request, 'account/login.html',{'name': 'Login page'})


def Logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('homepage')

