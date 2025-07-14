from django import forms

from Products.models import Product,Review

class Add_product_form(forms.ModelForm):

    class Meta:

        model=Product

        fields =['name','description','price','stock','category','image']


class Review_add_form(forms.ModelForm):

    class Meta:

        model=Review

        fields=['rating','review']      