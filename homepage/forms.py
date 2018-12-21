from django.contrib.auth.models import User;
from django import forms;
from .models import Reservation_Rest,Drinks_Item,FastFood_Item,Food_Item,Order_main,Order_secondary

class UserForm(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'input100','placeholder':'Username'}),required=True,max_length=100);
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'input100','placeholder':'Email'}),required=True,max_length=100);
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'input100','placeholder':'Password'}),required=True,max_length=50);
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'input100','placeholder':'Re-Password'}),required=True,max_length=50);
    class Meta:
        model=User;
        fields=['username','email','password'];


class ReservationForms(forms.ModelForm):
    fullname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control span12','placeholder':'Full Name'}),required=True,max_length=100);
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control span12','placeholder':'Email'}),required=True,max_length=100)
    date = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control span12','placeholder':'Date(yyyy-mm-dd)'}),required=True);
    time = forms.TimeField(widget=forms.TimeInput(attrs={'class':'form-control span12','placeholder':'Time(eg. 23:34)'}),required=True);
    party_size = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control span12','type':'number','placeholder':'Party Size'}),required=True);
    phone_no = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control span12','type':'number','placeholder':'Phone Number'}),required=True,max_length=100);
    class Meta:
        model=Reservation_Rest;
        fields=[
            'fullname',
            'email',
            'date',
            'time',
            'party_size',
            'phone_no'
        ];

class DrinksForms(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control span12','placeholder':'Drinks Name'}),required=True,max_length=100);
    price =forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control span12','type':'number','placeholder':'Price'}),required=True);
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control span12','placeholder':'About Drinks'}),required=True,max_length=100);

    class Meta:
        model = Drinks_Item;
        fields = [
            'name',
            'price',
            'content',
        ];


class FastFoodForms(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control span12','placeholder':'Fast Food Name'}),required=True,max_length=100);
    price =forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control span12','type':'number','placeholder':'Price'}),required=True);
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control span12','placeholder':'About Food'}),required=True,max_length=100);

    class Meta:
        model = FastFood_Item;
        fields = [
            'name',
            'price',
            'content',
        ];

class FoodForms(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control span12','placeholder':'Food Name'}),required=True,max_length=100);
    price =forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control span12','type':'number','placeholder':'Price'}),required=True);
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control span12','placeholder':'About Food'}),required=True,max_length=100);

    class Meta:
        model = Food_Item;
        fields = [
            'name',
            'price',
            'content',
        ];

class OrderMainForms(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control span12','placeholder':'Full Name'}),required=True,max_length=100);
    total = forms.IntegerField(
        widget=forms.TextInput(attrs={'class': 'form-control span12', 'type': 'number', 'placeholder': 'Total Price'}),
        required=True);
    class Meta:
        model = Order_main;
        fields = [
            'name',
            'total',
        ];

class OrderSecondaryForms(forms.ModelForm):
    food_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control span12','placeholder':'Food Name'}),required=True,max_length=100);
    price =forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control span12','type':'number','placeholder':'Price'}),required=True);

    class Meta:
        model = Order_secondary;
        fields = [
            'food_name',
            'price',
        ];

