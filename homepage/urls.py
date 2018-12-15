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
]
