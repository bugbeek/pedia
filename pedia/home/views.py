from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import Signupform
from django.contrib import messages

#piyush unwanted

def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request, 'index.html')

def loginuser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request,user)
        # A backend authenticated the credentials
            return redirect("/")
        else:
        # No backend authenticated the credentials
            return render(request,'login.html')

    return render(request,'login.html')

def logoutuser(request):
    logout(request)
    return redirect('/login')

def signup(request):

    if request.method == 'POST':
        fm = Signupform(request.POST)
        if fm.is_valid():
            messages.success(request,'Account created successfully')
            fm.save()
    else:
        fm = Signupform()
    return render(request,'signup.html', {'form':fm})