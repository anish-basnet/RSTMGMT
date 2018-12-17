from django.shortcuts import render,redirect,HttpResponseRedirect,render_to_response,get_object_or_404
from .content_information._index import as_list_index,main_info;
from .content_information._information import as_list_information;
from .content_information._payment import as_list_payment;
from .content_information._services import as_list_services;
from django.contrib.auth import authenticate,login;
from django.views.generic import View;
from django.contrib.auth.models import User;
from .forms import UserForm,ReservationForms,DrinksForms,FastFoodForms,FoodForms
from django.contrib import messages;
from django.conf import settings
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist

from .models import Reservation_Rest,Drinks_Item,FastFood_Item,Food_Item

user_name_current="";


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
                user_name_current=username;
                print(user_name_current)
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
    return render(request, 'dashboard/index.html',{'username':user_name_current})

def username_present(username):
    if User.objects.filter(username=username).exists():
        return True
    return False




#dashboard views also integrated
def delete_reserve(request,pk):
    u = Reservation_Rest.objects.get(pk=pk).delete()
    return HttpResponseRedirect('/dashboard/reserve_now')

def reserve_now(request):
    value_list=Reservation_Rest.objects.all();
    frm1=ReservationForms(request.POST or None);
    if(frm1.is_valid()):
        frm1.save();
        messages.success(request, 'Previous Form submission was successful');
        frm1=ReservationForms();
    return render(request,'dashboard/reserve_now.html',{'frm1':frm1,'table_fill_value':value_list,'username':user_name_current});


def drinks_item(request):
    value_list=Drinks_Item.objects.all();
    frm1=DrinksForms(request.POST or None);
    if(frm1.is_valid()):
        frm1.save();
        messages.success(request,'Previous Item Sucessfully added!');
        frm1=DrinksForms();
    return render(request,'dashboard/drinksitem.html',{'frm1':frm1,'table_fill_value':value_list,'username':user_name_current});

def delete_drinks(request,pk):
    u = Drinks_Item.objects.get(pk=pk).delete()
    #return render(request, 'dashboard/drinksitem.html', {'frm1': frm1, 'table_fill_value': value_list});
    return HttpResponseRedirect('/dashboard/drinks_item');

def fast_food(request):
    value_list = FastFood_Item.objects.all();
    frm11 = FastFoodForms(request.POST or None);
    if (frm11.is_valid()):
        frm11.save();
        messages.success(request, 'Previous Item Sucessfully added!');
        frm11 = FastFoodForms();
    return render(request, 'dashboard/fastfooditem.html', {'frm1': frm11, 'table_fill_value': value_list,'username':user_name_current});

def delete_fastfood(request,pk):
    u = FastFood_Item.objects.get(pk=pk).delete()
    #return render(request, 'dashboard/drinksitem.html', {'frm1': frm1, 'table_fill_value': value_list});
    return HttpResponseRedirect('/dashboard/fast_food');

def food(request):
    value_list = Food_Item.objects.all();
    frm11 = FoodForms(request.POST or None);
    if (frm11.is_valid()):
        frm11.save();
        messages.success(request, 'Previous Item Sucessfully added!');
        frm11 = FoodForms();
    return render(request, 'dashboard/food.html', {'frm1': frm11, 'table_fill_value': value_list,'username':user_name_current});

def delete_food(request,pk):
    u = Food_Item.objects.get(pk=pk).delete()
    #return render(request, 'dashboard/drinksitem.html', {'frm1': frm1, 'table_fill_value': value_list});
    return HttpResponseRedirect('/dashboard/food');