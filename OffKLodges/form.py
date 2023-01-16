from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from .models import Profile, Payment, FindRoomMate
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={
                'class':"form-control", 'style':'max-width: 400px;',
                'placeholder': 'Wizkid'
            }),
            'email': forms.EmailInput(attrs={
                'class':"form-control", 'style':'max-width: 400px;',
                'placeholder': 'Wizkid@gmail.com'
            }),
            'password1': forms.PasswordInput(attrs={
                'class':"form-control", 'style':'max-width: 400px;',
                'placeholder': "********"
            }),
            'password2': forms.PasswordInput(attrs={
                'class':"form-control", 'style':'max-width: 400px;',
                'placeholder': "********"
            })
        }
        

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount', 'email']

class FindRoomMateForm(forms.ModelForm):
    class Meta:
        model = FindRoomMate
        
        fields = ['fname', 'lname', 'phone_number', 'email_i', 'state', 'sex',
                'level','earlywake', 'noise', 'organizedSpace', 'grocries', 
                'personalSpace', 'disabilites']
        labels = {
            'fname':'First Name:',
            'lname':'Surname',
            'phone_number':'Phone Number',
            'email_i':'Email',
            'state':'State', 
            'sex':'Sex',
            'level':'Level',
            'earlywake':'Do you prefer to go to bed early or stay up late?', 
            'noise':'Do you like to study in silent or with background noise?', 
            'organizedSpace':'Do you like to keep your living space clean and organized?', 
            'grocries':'Do you expect to share groceries and household items?', 
            'personalSpace':'Do you prefer to spend a lot of time with your roommte, or do you prefer to have your own space and time?', 
            'disabilites':'Do you have any allergies, disabilities, or others?'
        }

        widgets = {
            'fname': TextInput(attrs={
                'class':"form-control",
            }),
            'lname': TextInput(attrs={
                'class':"form-control",
            }),
            'phone_number': TextInput(attrs={
                'class':"form-control",
            }),
            'email_i': TextInput(attrs={
                'class':"form-control",
            }),
            'state': forms.Select(attrs={
                'class':"form-select",
            }),
            'sex': forms.Select(attrs={
                'class':"form-select",
            }),
            'level': forms.Select(attrs={
                'class':"form-select",
            }),
            'earlywake': forms.Select(attrs={
                'class':"form-select",
            }),
            'noise': forms.Select(attrs={
                'class':"form-select",
            }),
            'organizedSpace': forms.Select(attrs={
                'class':"form-select",
            }),
            'grocries': forms.Select(attrs={
                'class':"form-select",
            }),
            'personalSpace': forms.Select(attrs={
                'class':"form-select",
            }),
            'disabilites': forms.Select(attrs={
                'class':"form-select",
            })
        }