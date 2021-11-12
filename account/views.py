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


def Profile(request):
    if not request.user.is_authenticated:
        return render(request, 'account/home.html',{'name': 'Home page','error':'Please login first!'})
    else:
        naam = request.user.username
        cur_user = User.objects.get(username=naam)
        return render(request, 'account/profilepage.html',{'name': 'Profile page', 'user': cur_user})


def Update_profile(request):
    if not request.user.is_authenticated:
        return render(request, 'account/home.html',{'name': 'Home page','error':'Please login first!'})
    else:
        if request.method == 'POST':
            username = request.user.username
            User.objects.filter(username= username).update( email = request.POST['email'], first_name=request.POST['fname'], last_name=request.POST['lname'])
            return redirect('profilepage')
        else:
            return render(request, 'account/updateprofile.html',{'name': 'Update Profile'})


