"""
URL configuration for Ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from user_application import views
from Products.views import*
from order.views import*
from Ecommerce import settings
from django.conf.urls.static import static

def redirect_home(request):

    return redirect('home')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',redirect_home),
    path('Ecommerce',views.BaseView.as_view(),name='home'),
    path('user_application/register/',views.Register_view.as_view(),name='register'),
    path('user_application/login/',views.Login_view.as_view(),name='login'),
    path('user_application/logout/',views.Signout.as_view(),name="logout"),


    path('user_application/forgot/',views.ForgotPasswordView.as_view(),name="forgot"),
    path('user/reset/',views.ResetPassword_view.as_view(),name="reset"),
    path('user/otp_verify/',views.Otp_verify.as_view(),name="otp_verify"),


    path('product/add_category/',Addcategory.as_view(),name='add_category'),
    path('product/update_category/<int:pk>/',UpdateCategory_view.as_view(),name='update_category'),
    path('product/category_list/',Category_listview.as_view(),name='category_list'),
    path('product/delete_category/<int:pk>',Category_deleteview.as_view(),name='category_delete'),
    path('product/category_detail/<int:pk>',Category_detail.as_view(),name='category_detail'),


    path('product/add_product/',Add_productview.as_view(),name='add_product'),
    path('product/update_product/<int:pk>',Update_productview.as_view(),name='update_product'),
    path('product/product_list/',Product_listview.as_view(),name='product_list'),
    path('product/delete_product/<int:pk>',Product_deleteview.as_view(),name='product_delete'),
    path('product/product_detail/<int:pk>',ProductDetailview.as_view(),name='product_detail'),

    path('product/add_review/<int:pk>',Add_review_view.as_view(),name='add_review'),
    path('product/review_list/',Review_list_view.as_view(),name='review_list'),
    path('product/review_delete/<int:pk>',Review_delete.as_view(),name='review_delete'),
    path('product/review_detail/<int:pk>',Review_detail_view.as_view(),name='review_detail'),

    path('product/add_cart/<int:pk>',Cart_add_view.as_view(),name='add_cart'),
    path('product/cart_list/',CartitemListView.as_view(),name='cartlist'),
    path('product/update_cart/<int:pk>',CartItemUpdateView.as_view(),name='update_cart'),
    path('product/delete_cart/<int:pk>',Cartdelete.as_view(),name='delete_cart'),


    path('product/add_order/<int:pk>',AddOrderProduct.as_view(),name='add_order'),
    path('product/add_cart_order/',Addorder_cart.as_view(),name='cart_order'),

    path('product/search/',SearchFilter.as_view(),name='search'),

    path('product/myorderitem/',OrderitemlistView.as_view(),name='myorderitem'),
    path('product/placeorderview/',PlaceorderView.as_view(),name='placeorder'),
    path('product/paymentsuccess/',PaymentSuccessView.as_view(),name='paymentsuccess'),

    path('api/',include('api.urls')),






    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#lnzs hsqq hjef nabj