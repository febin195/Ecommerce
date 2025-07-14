from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated

from api.serializers import Userserializer,CartSerializer

from user_application.models import User

from Products.models import Product

from rest_framework import status

from Products.models import Cart,CartitemModel
from order.models import Order



from django.core.mail import send_mail

# Create your views here.


class Register(APIView):

    def post(self,request):

        serializer=Userserializer(data=request.data)

        if serializer.is_valid():

            user=User.objects.create_user(**serializer.data)

            Cart.objects.create(user=user)

            Order.objects.create(user=user)

            

            

            subject='welcome mail'

            message=f'haii welcome to my application'

            from_email='muhammadfebin4@gmail.com'

            recipient_list=[serializer.data.get('email')]

            send_mail(subject,message,from_email,recipient_list,fail_silently=True)

            return Response({'message':'user created successfully'},status=status.HTTP_201_CREATED)

        return Response({'message':'not created'},status=status.HTTP_401_UNAUTHORIZED)    
    

class AddtoCartApi(APIView):

    permission_classes=[IsAuthenticated]

    def post(self,request):

        serializer=CartSerializer(data=request.data)

        if serializer.is_valid():

            product_id=serializer.validated_data.get('cart_item')

            quantity=serializer.validated_data.get('quantity')

            cart=Cart.objects.get(user=request.user)

            product=Product.objects.get(id=product_id)

            CartitemModel.objects.create(cart=cart,cart_item=product,quantity=quantity)

            return Response({'message':'added to cart'})
        
        return Response({'message':'no added'})

