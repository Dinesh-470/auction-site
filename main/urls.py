from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name="index"),
    path('login/',views.login,name="login"),
    path('register/',views.register,name="register"),
    path('auctions/',views.auctions,name="auctions"),
    path('auction/<str:auction_name>',views.auction,name="auction"),
    path('user/',views.user,name="user"),
    path('user/upload',views.product_upload,name="product_upload"),
    path('user/my_products',views.my_products,name="my_products"),
    path('user/upload/done',views.product_upload_done,name="product_uploaded"),
    path('user/<str:user_name>',views.user_inspect,name="user_inspect"),
    path('user/login/',views.user_login),
    path('user/register/',views.user_register),
    path('404/',views.error,name="error")
]