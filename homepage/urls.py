from django.conf.urls import url
from . import views
from django.urls import path,include

app_name='homepage'
urlpatterns = [
    path('', views.index, name='index'),
    path('news/',views.news,name='news'),
    path('information/',views.information,name='information'),
    path('menu/',views.menu,name='menu'),
    path('services/',views.services,name='services'),
    path('reservation/',views.reservation,name='reservation'),
    path('payment/',views.payment,name='payment'),
    path('login/',views.loginn,name='login'),
    path('signup/',views.signup,name='signup'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('dashboard/reserve_now',views.reserve_now,name='reserve_now'),
    path('dashboard/reserve_now/<int:pk>/',views.delete_reserve,name='delete_reserve'),
    path('dashboard/drinks_item',views.drinks_item,name='drinks_item'),
    path('dashboard/drinks_item/<int:pk>/', views.delete_drinks, name='delete_drinks'),
    path('dashboard/fast_food',views.fast_food,name='fast_food'),
    path('dashboard/fast_food/<int:pk>/',views.delete_fastfood,name='delete_fastfood'),
    path('dashboard/food',views.food,name='food'),
    path('dashboard/food/<int:pk>/', views.delete_food, name='delete_food'),
    path('dashboard/<int:pk>/', views.delete_bills, name='delete_bills'),
]
