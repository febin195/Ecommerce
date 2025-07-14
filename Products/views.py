from django.shortcuts import render,redirect

from django.urls import reverse_lazy

from Products.models import Categorymodel,Product,Review,CartitemModel,Cart

from user_application.models import User

from Products.forms import Add_product_form,Review_add_form

from django.views.generic import View,CreateView,UpdateView,ListView,DeleteView,DetailView

from django.utils.decorators import method_decorator

from django.db import IntegrityError

# Create your views here.

def is_user(fn):

    def wrapper(request,**kwargs):

        id=kwargs.get('pk')

        data=User.objects.get(id=id)

        if data.id==request.user:

            return fn(request,**kwargs)
        
        return redirect('login')
    
    return wrapper


def user_login(fn):

    def wrapper(request,**kwargs):

        if not request.user.is_authenticated:

            return redirect('login')
        
        else:

            return fn(request,**kwargs)
        
    return wrapper    



#url >> lh:8000/product/addcategory

class Addcategory(CreateView):

    model=Categorymodel

    template_name='add_category.html'

    fields ="__all__"

    success_url=reverse_lazy('login')



#url >> lh:8000/product/updatecategory

class UpdateCategory_view(UpdateView):

    model=Categorymodel

    template_name='categoryupdate.html'

    fields="__all__"

    success_url=reverse_lazy('login')


#url >> lh:8000/product/categorylist

class Category_listview(ListView):

    model=Categorymodel

    template_name='cateogry_list.html'

    context_object_name='data'

    success_url=reverse_lazy('regisetr') 


#url >> lh:8000/product/category_delete

class Category_deleteview(DeleteView):

    model=Categorymodel

    template_name='categorymodel_confirm_delete.html'

    success_url=reverse_lazy('add_product')


#url >> lh:8000/product/category_detail

class Category_detail(DetailView):

    model=Categorymodel

    template_name='category_detail.html'

    context_object_name='data'

        

#url >> lh:8000/product/addproductview

class Add_productview(CreateView):

    model=Product

    template_name='add_product.html'

    form_class=  Add_product_form

    success_url=reverse_lazy('register')

#url >> lh:8000/product/updateproductview

class Update_productview(UpdateView):

    model=Product

    template_name='update_product.html'

    fields=['name','description','price','stock','category','image'] 

    success_url=reverse_lazy('add_product')  

#url >> lh:8000/product/productlist

class Product_listview(ListView):

    model=Product

    template_name='product_list.html'

    context_object_name='data'

    

#url >> lh:8000/product/product_delete

class Product_deleteview(DeleteView):

    model=Product

    template_name='productmodel_confirm_delete.html'

    success_url=reverse_lazy('add_product') 

#url >> lh:8000/product/productdetail

class ProductDetailview(DetailView):

    model=Product

    template_name='productdetail.html'

    context_object_name='data'

    success_url=reverse_lazy('add_product')    

#url >> lh:8000/product/add_review/int:pk


class Add_review_view(View):

    def get(self,request,**kwargs):

        id=kwargs.get('pk')

        data=Product.objects.get(id=id)
        

        form=Review_add_form

        return render(request,'add_review.html',{'form':form})
    

    def post(self,request,**kwargs):

        id=kwargs.get('pk')

        data=Product.objects.get(id=id)

        form=Review_add_form(request.POST)

        if form.is_valid():

            Review.objects.create(**form.cleaned_data,user_id=request.user,product_id=data)

            return redirect('product_list')
        

class Review_list_view(ListView):

    model=Review

    template_name='review_list.html'

    context_object_name='data' 


class Review_delete(DeleteView):

    model=Review

    template_name='review_delete.html'

    success_url=reverse_lazy('review_list')


class Review_detail_view(DetailView):

    model=Review

    template_name='review_detail.html'

    context_object_name='data'



    

class Cart_add_view(View):

    

    def get(self,request,**kwargs):

        id=kwargs.get('pk')

        item=Product.objects.get(id=id)

        if item.stock > 0:

            cart=Cart.objects.get(user=request.user)

            try: 
                CartitemModel.objects.create(cart=cart,cart_item=item)
            
                print(cart.total_price)

            except IntegrityError:

                return redirect('cartlist')


        return redirect('cartlist')           



            
            

@method_decorator(decorator=user_login,name='dispatch')
class CartitemListView(View):

    def get(self,request):

        cart=Cart.objects.get(user=request.user)

        data=CartitemModel.objects.filter(cart=cart)

        list=[]

        for i in data:

            subtotal=i.cart_item.price * i.quantity 

            list.append(subtotal)

        c_item=zip(data,list)

        print(c_item)

        print(cart.total_price)

        return render(request,'cartlist.html',{'c_items':c_item,'total_price':cart.total_price})    



class CartItemUpdateView(View):

    def post (self,request,**kwargs):
        
        id = kwargs.get('pk')

        new_quantity = int(request.POST.get("quantity"))
        print(request.POST.get("quantity"))
        data =  CartitemModel.objects.get(id=id)

        if data.quantity  > data.cart_item.stock:

            data.quantity=data.cart_item.stock

            data.save()

        else:

            data.quantity= new_quantity

            data.save()

        return redirect('cartlist')       


class Cartdelete(View):

    def get(self,request,**kwargs):

        id=kwargs.get('pk')

        cart=Cart.objects.get(user=request.user)

        data=CartitemModel.objects.get(id=id,cart=cart)

        if data:

            data.delete()



        return redirect('cartlist')


class SearchFilter(View):

    def get(self,request):

        query=request.GET.get('q')

        data=Product.objects.filter(name__icontains=query)

        return render(request,'product_list.html',{'data':data})