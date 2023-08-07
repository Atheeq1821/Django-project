from imaplib import _Authenticator
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
# Create your views here.
def signupview(request):
    if(request.method=='POST'):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username):
            messages.error(request," Username already exists")
            return redirect("signup")
        
        if User.objects.filter(email=email):
            messages.error(request,"Email already exists")
            return redirect("signup")
        
        if len(username)<5:
            messages.error(request,"Username must contains atleast 5 characters")

        if not username.isalnum():
            messages.error(request,"Username should not contains special characters")
            return redirect("signup")
        
        newuser = User.objects.create_user(username,email,password)
        newuser.save()
        messages.success(request," Your account has been successfully Created.")
        return redirect('login')
    return render(request,'signup.html')
def loginview(request):
    if(request.method=='POST'):
         username = request.POST['username']
         password = request.POST['password']
         user = authenticate(username=username, password= password)
         if user is not None:
            login(request,user)   
            peyar=user.username
            return render(request,'homepage.html',{
                "name":peyar
            })
         else:
             messages.error(request,"Bad Credentials")  
             return redirect("login") 
    return render(request,'login.html')
def homepageview(request):
    return render(request,'homepage.html')
