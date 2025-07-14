from django import forms

from user_application.models import User




class Userform(forms.Form):

    
    username=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter user name'}))

    first_name=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your firstname'}))

    last_name=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your lastname'}))

    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':"Enter your password"}))

    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter your Email'})) 

class Loginform(forms.Form):    

    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your username'}))

    password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your password'}))

class ForgotForm(forms.Form):

    username=forms.CharField(max_length=100)

   

class Otpform(forms.Form):

    otp=forms.CharField(max_length=10)  


class Reset_form(forms.Form): 

    new_password=forms.CharField(max_length=100)

    confirm_password=forms.CharField(max_length=100)        


