from django.shortcuts import render,redirect,HttpResponseRedirect
from .content_information._index import as_list_index,main_info;
from .content_information._information import as_list_information;
from .content_information._payment import as_list_payment;
from .content_information._services import as_list_services;
from django.contrib.auth import authenticate,login;
from django.views.generic import View;
from django.contrib.auth.models import User;
from .forms import UserForm;
from django.contrib import messages;
from django.core.exceptions import ObjectDoesNotExist

def index(request):
    deck_list=as_list_index();
    return render(request, "homepage/index.html",context={'main_info':main_info,
                                                          'deck_list_info':deck_list})

def news(request):
    return render(request,"homepage/news.html");

def information(request):
    info_list=as_list_information();
    return render(request,"homepage/information.html",context={'info_list':info_list});

def menu(request):
    return render(request,'homepage/menu.html');

def services(request):
    info_list=as_list_services();
    return render(request,'homepage/services.html',context={'info_list':info_list});

def reservation(request):
    return render(request,'homepage/reservation.html')

def payment(request):
    info_list1=as_list_payment();
    return render(request,'homepage/payment.html',context={'info_list':info_list1})

def loginn(request):
    if(request.method=='POST'):
        username=request.POST['user'];
        password=request.POST['pass'];
        try:
            user1=authenticate(username=username,password=password);
            if(user1 is not None):
                login(request,user1);
                print("Entered");
                return HttpResponseRedirect('/dashboard/');
            else:
                messages.error(request,'Username and password did not matched');
        except(ObjectDoesNotExist):
            print('Invalid User');
    return render(request,'homepage/login.html');

def signup(request):
    if(request.method=='POST'):
        form1=UserForm(request.POST);
        if(form1.is_valid()):
            username=form1.cleaned_data['username'];
            email=form1.cleaned_data['email'];
            password=form1.cleaned_data['password'];
            User.objects.create_user(username=username,email=email,password=password);
            messages.error(request,"Sucessfully Sign Up!");
            return HttpResponseRedirect('/signup/');
        else:
            form1=UserForm();
    else:
        form1=UserForm();
    return render(request,'homepage/signup.html',{'frm':form1});

def dashboard(request):
    return render(request,'homepage/dashboard.html')

def username_present(username):
    if User.objects.filter(username=username).exists():
        return True
    return False