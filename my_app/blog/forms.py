from django import forms
from blog.models import UserDb
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import item
from django_countries.fields import CountryField


class UserDbForm(forms.ModelForm):
    class Meta:
        model = UserDb
        fields = '__all__'


class Searchform(forms.ModelForm):
    class Meta:
        model = item
        fields = ['items_name']


PAYMENT_CHOICES = (
    ('B', 'Bank Account'),
    ('M', 'Mobile Money')
)


class CheckoutForm(forms.Form):
    First_name = forms.CharField()
    Last_name = forms.CharField()
    Email = forms.EmailField()
    Country = CountryField(blank='(select country)').formfield()
    street_address = forms.CharField()
    Apartment_address = forms.CharField(required=False)
    Town_or_City = forms.CharField()
    Zip = forms.CharField()
    Phone = forms.IntegerField()
    same_billing_address = forms.BooleanField(widget=forms.CheckboxInput())
    save_info = forms.BooleanField(widget=forms.CheckboxInput())
    payment_option = forms.ChoiceField(widget=forms.RadioSelect(), choices=PAYMENT_CHOICES)
    save_as_birthday = forms.BooleanField(required=False, widget=forms.CheckboxInput())


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']