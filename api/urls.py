
from django.urls import path

from api.views import *

from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns=[
    path('register',Register.as_view()),

    path('token',TokenObtainPairView.as_view()),

    path('refresh/token',TokenRefreshView.as_view()),

    path('addcart',AddtoCartApi.as_view()),



]