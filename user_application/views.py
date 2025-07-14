from django.shortcuts import render,redirect

from user_application.models import User

from Products.models import Cart,Categorymodel,Product

from order.models import Order

from user_application.forms import Userform,Loginform,ForgotForm,Otpform,Reset_form

from django.views.generic import View

from django.contrib.auth import authenticate,login,logout

from django.core.mail import send_mail

import random

# Create your views here.

class BaseView(View):

    def get(self,request):

        data=Product.objects.all()

        return render(request,'base.html',{'data':data})

# url >> lh:8000/user_application/register

class Register_view(View):

    def get(self,request):

        form=Userform

        return render(request,'register.html',{'form':form})
    
    def post(self,request):

        form=Userform(request.POST)

        if form.is_valid():

            user=User.objects.create_user(**form.cleaned_data)

            Cart.objects.create(user=user)

            Order.objects.create(user=user)

            

            

            subject='welcome mail'

            message=f'haii welcome to my application'

            from_email='muhammadfebin4@gmail.com'

            recipient_list=[form.cleaned_data.get('email')]

            send_mail(subject,message,from_email,recipient_list,fail_silently=True)



        form=Userform

        return redirect('login')
    

#  url >> lh:8000/user_application/login


class Login_view(View):

    def get(self,request):

        form=Loginform

        return render(request,'login.html',{'form':form})
    
    def post(self,request):

        form=Loginform(request.POST)

        if form.is_valid():

            username=form.cleaned_data.get('username')

            password=form.cleaned_data.get('password')

            user=authenticate(request,username=username,password=password)

            if Loginform:

                login(request,user)

                return render(request,'base.html')
            
            else:

                return render(request,'register.html')



class Signout(View):

    def get(self,request):

        logout(request)

        return redirect('login')
    

class ForgotPasswordView(View):

    def get(self,request):

        form=ForgotForm

        return render(request,'forgot.html',{'form':form})

    def post(self,request):

        username=request.POST.get('username')

        user=User.objects.get(username=username)

        if user:

            otp=random.randint(1000,9999)

            request.session['username']=username

            request.session['otp']=otp 

            send_mail(subject='reset password otp',message=str(otp),from_email='muhammadfebin4@gmail.com',recipient_list=[user.email])

            return redirect('otp_verify')  


class Otp_verify(View):

    def get(self,request):

        form=Otpform

        return render(request,'otp_verify.html',{'form':form})
    
    def post(self,request):

        new_otp=request.POST.get('otp')

        old_otp=request.session.get('otp')

        if str(new_otp)==str(old_otp):

            return redirect('reset')



class ResetPassword_view(View):

    def get(self,request):

        form=Reset_form

        return render(request,'resetpassword.html',{'form':form})
    
    def post(self,request):

        c_password=request.POST.get('confirm_password')

        n_password=request.POST.get('new_password')

        if c_password==n_password:

            u_name=request.session.get('username')

            user=User.objects.get(username=u_name)

            user.set_password(n_password)

            user.save()

        return redirect('login')    






