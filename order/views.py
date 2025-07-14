from django.shortcuts import render,redirect

from django.views.generic import View

from Products.models import Product,Cart,CartitemModel

from order.models import Order,OrderItem,Order_summary

from django.views.decorators.csrf import csrf_exempt

from django.utils.decorators import method_decorator

# Create your views here.

class AddOrderProduct(View):

    def get(self,request,**kwargs):

        id = kwargs.get('pk')

        item=Product.objects.get(id=id)

        return render(request,'orderpage.html',{'item':item})
    
    def post(self,request,**kwargs):

        id=kwargs.get('pk')

        item=Product.objects.get(id=id)

        quantity=request.POST.get("quantity")

        total = quantity * int(item.price)

        user_id=Order.objects.get(user=request.user)

        OrderItem.objects.create(order_id=user_id,quantity=quantity,item=item,status='pending')

        return render(request,'orderpage.html',{'total':total})
    

class Addorder_cart(View):

    def get(self,request):

        user=Cart.objects.get(user=request.user)

        items=CartitemModel.objects.filter(cart=user)

        total=Cart.total_price

        user=Order.objects.get(user = request.user)

        for i in items:

            OrderItem.objects.create(order_id=user,item=i.cart_item,quantity=i.quantity,status='pending')

        items.delete()


        return render(request,'orderpage.html',{'total':total}) 
    

class OrderitemlistView(View):

    def get(self,request):

        data=OrderItem.objects.filter(order_id=request.user.id,status='pending')

        return render(request,'myorderitems.html',{'data':data})


import razorpay


class PlaceorderView(View):

    def get(self,request):

        #authentication in between webserver and razorpay

        client = razorpay.Client(auth=("rzp_test_4TAHT0kAH5sniL", "L2TEs1ZqN5iuWWYEgE8vrgVa"))

        user = request.user

        user=Order.objects.get(user=user)

        order_items=OrderItem.objects.filter(order_id=user,status='pending')

        total=sum(i.quantity*i.item.price for i in order_items)

        new_amonut=int(total*100)

        data=client.order.create(data={
             
                                  "amount":new_amonut,
                                  "currency": "INR"})
        
        print(data)

        # saving the response to the order summary

        summary=Order_summary.objects.create(user=user,order_id=data['id'],total=data['amount'])

        context={'summary':summary,'order_items':order_items,'razorpaykeyid':"rzp_test_4TAHT0kAH5sniL",'orderid':data['id'],
                 'amount':data['amount'],'username':'febin'}




        return render(request,'payment.html',context)
    
#{'amount': 10629900, 'amount_due': 10629900, 'amount_paid': 0, 'attempts': 0, 'created_at': 1744111419, 'currency': 'INR', 'entity': 'order', 'id': 'order_QGXspgOxgbtpz4', 'notes': [], 'offer_id': None, 'receipt': None, 'status': 'created'}

@method_decorator(decorator=csrf_exempt,name='dispatch')     
class PaymentSuccessView(View):

    def post(self,request):

        print(request.POST)

        user=Order.objects.get(user=request.user)

        summary=Order_summary.objects.filter(user=user,payment_status=False)

        for i in summary:

            i.payment_status=True

            i.save()

        items=OrderItem.objects.filter(order_id=user,status='pending')

        for i in items:

            i.status='completted'

            i.save()

        return render(request,'payment.html')
    
    #<QueryDict: {'razorpay_payment_id': ['pay_QGvKvIg14IkRAM'], 'razorpay_order_id': ['order_QGvKWeO21ZZh96'], 'razorpay_signature': ['688f8b3ec8483cf078b274223c868653ec873e9f0565bbab1bcf1f559efd2b13']}>




