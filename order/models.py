from django.db import models

from user_application.models import User

from Products.models import Product

# Create your models here.

class Order(models.Model):

    user=models.OneToOneField(User,on_delete=models.CASCADE)

    created_date=models.DateField(auto_now_add=True)

    


class OrderItem(models.Model):

    order_id=models.ForeignKey(Order,on_delete=models.CASCADE)   

    item=models.ForeignKey(Product,on_delete=models.CASCADE) 

    quantity=models.IntegerField(default=1)

    status=models.CharField(max_length=150,choices=[('pending','pending'),('completted','completted'),('cancelled','cancelled')])



class Order_summary(models.Model):

    # order_item_id=models.ForeignKey(OrderItem,on_delete=models.CASCADE,null=True)

    user=models.ForeignKey(Order,null=True,on_delete=models.CASCADE)

    order_id=models.CharField(max_length=100)

    payment_status=models.BooleanField(default=False)

    payment_id=models.CharField(max_length=100,null=True,blank=True)

    total=models.FloatField()

    date=models.DateField(auto_now_add=True)

