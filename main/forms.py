from django import forms
from .models import *
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={"class": "form-control"}))
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'email-bt', 'placeholder':'Name', "class": "form-control"}),
            'email': forms.EmailInput(attrs={'class': 'email-bt', 'placeholder':'Email'}),
            'phone' : forms.TextInput(attrs={'class':'email-bt', 'placeholder':'Phone'}),
            'message' : forms.Textarea(attrs={'class':'massage-bt', 'placeholder':'Massage', 'rows':'5'}),
        }
