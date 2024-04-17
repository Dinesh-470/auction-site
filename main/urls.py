from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name="index"),
    path('login/',views.login,name="login"),
    path('register/',views.register,name="register"),
    path('auctions/',views.auctions,name="auctions"),
    path('auction/<str:auction_name>',views.auction,name="auction"),
    path('user/',views.user,name="user"),
    path('user/<str:user_name>',views.user_inspect,name="user_inspect"),
]