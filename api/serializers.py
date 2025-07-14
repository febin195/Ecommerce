from rest_framework import serializers

from user_application.models import User

from Products.models import Cart,CartitemModel

class Userserializer(serializers.ModelSerializer):

    class Meta:

        model=User

        fields=['username','first_name','last_name','email','password']


class CartSerializer(serializers.Serializer):

    cart_item=serializers.IntegerField()

    quantity=serializers.IntegerField()



  
