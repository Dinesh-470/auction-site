from django.shortcuts import redirect
from django.template import loader
from django.http import HttpResponse
from . import models
from django.conf import settings
# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    context = {
        'login' : False,
        'name' : 'dinesh',
    }
    return HttpResponse(template.render(context,request))

def login(request):
    template = loader.get_template('login.html')
    context = {
    }
    return HttpResponse(template.render(context,request))

def register(request):
    template = loader.get_template('register.html')
    context = {

    }
    return HttpResponse(template.render(context,request))

def auctions(request):
    template = loader.get_template('auctions.html')
    context = {
        'data' : [1,2,3,4,5,6]
    }
    return HttpResponse(template.render(context,request))

def auction(request,auction_name):
    template = loader.get_template('auction.html')
    context = {
        'product_id':auction_name,
        'user_name' : "dineshreddy",
        'base_price' : 500,
        'current_bid' : 1000,
        'activity' : [
            {
            'user_name' : 'dineshreddypaidi',
            'price' : 900,},
            {
            'user_name' : 'someuser1',
            'price' : 850,},
            {
            'user_name' : 'someuser2',
            'price' : 820,},
            {
            'user_name' : 'paididineshreddy',
            'price' : 800,},
            {
            'user_name' : 'dineshreddypaidi',
            'price' : 700,},
            {
            'user_name' : 'dineshreddypaidi470',
            'price' : 600,},
                    ]
    }
    return HttpResponse(template.render(context,request))

def user(request):
    user_details = models.user.objects.get(pk="dinesh")
    template = loader.get_template('user.html')
    context = {
        'name' : user_details.user_name,
        'image' : user_details.user_image,
    }
    return HttpResponse(template.render(context,request))

def user_inspect(request,user_name):
    return HttpResponse(user_name)

def user_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        if user_name == 'dinesh' and password == 'dinesh':
            settings.LOGGED_IN =True
            return redirect('/')
        else:
            return redirect('/login/',message="user not found")
    else:
        return HttpResponse("error")
        
def user_register():
    pass