from tkinter import Widget
from turtle import width
from django import forms
from allauth.account.forms import SignupForm, LoginForm, PasswordField
from .models import User


GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget = forms.EmailInput(attrs={
            'placeholder': 'Enter e-mail',
            'class':'form-control'
        })
        self.fields['password1'].widget = forms.PasswordInput(attrs={
            'placeholder': 'Enter password',
            'class':'form-control'
        })
        self.fields['password2'].widget = forms.PasswordInput(attrs={
            'placeholder': 'Enter password again',
            'class':'form-control'
        })

    field_order = ['email', 'name', 'gender', 'date_of_birth', 'address', 'password1', 'password2']

    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(
        attrs={
            'class': 'form-control'
        }))
    address = forms.CharField(max_length=254, widget=forms.TextInput(
        attrs={
            'placeholder': 'Enter address',
            'class': 'form-control'
        }))
    date_of_birth = forms.DateField(widget=forms.DateInput(
        attrs={
            'placeholder': 'YYYY-MM-DD',
            'class': 'form-control'
        }))
    name = forms.CharField(max_length=254, widget=forms.TextInput(
        attrs={
            'placeholder': 'Enter fullname',
            'class': 'form-control'
        }))
    

    def save(self, request):
        print("CHECK THIS OUT")
        print(request.get_full_path)
        user = super(CustomSignupForm, self).save(request)
        user.email = self.cleaned_data["email"]
        user.gender = self.cleaned_data["gender"]
        user.address = self.cleaned_data["address"]
        user.date_of_birth = self.cleaned_data["date_of_birth"]
        user.name = self.cleaned_data["name"]
        user.user_type = "CUSTOMER"
        user.save()
        return user

class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['remember'].widget = forms.HiddenInput()
        self.fields['login'].widget = forms.EmailInput(attrs={
            'placeholder': 'Enter e-mail',
            'class':'form-control'
        })
        self.fields['password'].widget = forms.PasswordInput(attrs={
            'placeholder': 'Enter password',
            'class':'form-control'
        })

    def save(self, request):
        user = super(CustomLoginForm, self).save(request)
        return user

class UpdateUserDetails(forms.ModelForm):
    class Meta:
        model = User
        fields = ['gender', 'address', 'date_of_birth', 'name']
        
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(
        attrs={
            'class': 'form-control'
        }))
    address = forms.CharField(max_length=254, widget=forms.TextInput(
        attrs={
            'placeholder': 'Enter address',
            'class': 'form-control'
        }))
    date_of_birth = forms.DateField(widget=forms.DateInput(
        attrs={
            'placeholder': 'YYYY-MM-DD',
            'class': 'form-control'
        }))
    name = forms.CharField(max_length=254, widget=forms.TextInput(
        attrs={
            'placeholder': 'Enter fullname',
            'class': 'form-control'
        }))

class ShopUserSignUpForm(CustomSignupForm):
    shopname = forms.CharField(max_length=254, widget=forms.TextInput(
        attrs={
            'placeholder': 'Enter fullname',
            'class': 'form-control'
        }))