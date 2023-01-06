from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from .models import Profile, Payment, FindRoomMates
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        

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
        model = FindRoomMates
        fields = ['fname', 'lname', 'email', 'state', 'sex',
                'level','earlywake', 'noise', 'organizedSpace', 'grocries', 
                'personalSpace', 'disabilites']
        labels = {
            'fname':'First Name:',
            'lname':'Surname',
            'email':'Email',
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