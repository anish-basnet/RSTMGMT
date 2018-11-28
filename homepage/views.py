from django.shortcuts import render
from .content_information._index import as_list_index,main_info;
from .content_information._information import as_list_information;
from .content_information._payment import as_list_payment;
from .content_information._services import as_list_services;

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

def login(request):
    return render(request,'homepage/login.html');

def signup(request):
    return render(request,'homepage/signup.html')