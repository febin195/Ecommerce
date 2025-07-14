from django.db import models

from user_application.models import User

# Create your models here.
class Categorymodel(models.Model):

    name = models.CharField(max_length=100)

    description=models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):

    name = models.CharField(max_length=100)

    description = models.TextField()

    price = models.DecimalField(max_digits=10 ,decimal_places=2)

    stock = models.PositiveIntegerField()

    category = models.ForeignKey(Categorymodel,on_delete=models.CASCADE)

    image = models.ImageField(upload_to='product_image')

    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Review(models.Model):

    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)

    rating=models.IntegerField(default=0,choices=[(i,i) for i in range(1,6)])

    review=models.TextField(max_length=100)

    created_date=models.DateField(auto_now_add=True)


class Cart(models.Model):

    user=models.OneToOneField(User,on_delete=models.CASCADE)

    created_date=models.DateField(auto_now_add=True)
    
    @property
    def total_price(self):

        return sum(i.cart_item.price * i.quantity for i in self.cartitemmodel_set.all())
    
    

    # @property
    # def total_quantity(self):

    #     return sum(item for item in self.cartitem_set.all())

class CartitemModel(models.Model):

    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)

    cart_item=models.ForeignKey(Product,on_delete=models.CASCADE)

    quantity=models.PositiveIntegerField(default=1)

    class Meta:

        unique_together=('cart','cart_item')


