from django.shortcuts import redirect
from django.template import loader
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from . import models
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
# Create your views here.
def index(request):
    logged_in = True if settings.LOGGED_IN else False
    product= models.Product.objects.order_by('-num_of_bids')[:10]
    data = {}
    for dt in product:
        image = models.Product_images.objects.filter(product_id=dt.product_id).first()
        data[dt] = image
    template = loader.get_template('index.html')
    context = {
        'login' : logged_in,
        'data' : data,
    }
    if logged_in:
        user_name = settings.USER_NAME 
        user = models.users.objects.get(user_name=user_name)
        context['user'] = user
        
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

def user_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = models.users.objects.get(user_name=user_name)
        except:
            return redirect('/404/')    
        if password == user.password:
            settings.LOGGED_IN =True
            settings.USER_NAME = user.user_name
            return redirect('/')
        else:
           return HttpResponse('password wrong.')
    else:
        return HttpResponse("error")
        
def user_register(request):
    if request.method == 'POST':
       username = request.POST.get('username')
       full_name = request.POST.get('name')
       email = request.POST.get('email')
       number = request.POST.get('number') 
       password1 = request.POST.get('password')
       password2 = request.POST.get('password2')
       image = request.FILES.get('image')
       try:
          user_namee = models.users.objects.get(user_name=username)
       except:
           user_namee = None
       if len(username) > 8:
            if user_namee == None:
                if password1 == password2:
                    user = models.users(
                        user_name = username,
                        full_name = full_name,
                        email = email,
                        number = number,
                        password = password1,
                        image = image,
                    )
                    user.save()
                    settings.LOGGED_IN =True
                    settings.USER_NAME = user.user_name
                    return redirect('/')
                else:
                    message = "password did't match"
            else:
                message = "user name already exist" 
       else:
            message = "user_name is too short atleast 8 charaters"     
       return HttpResponse(message)
   
def auctions(request):
    data = models.Product.objects.all().order_by('-num_of_bids')
    image_set = {}
    for dt in data:
        image = models.Product_images.objects.filter(product_id=dt.product_id).first()
        image_set[dt] = image
    template = loader.get_template('auctions.html')
    context = {
        'data' : image_set,
    }
    return HttpResponse(template.render(context,request))

def auction(request,auction_name):
    data = models.Product.objects.get(product_id=auction_name)
    image = models.Product_images.objects.filter(product_id=auction_name).first()
    template = loader.get_template('auction.html')
    context = {
        'data' : data,
        'image' : image,
    }
    return HttpResponse(template.render(context,request))

def user(request):
    if settings.LOGGED_IN == False:
        return redirect('/login')
    user_details = models.users.objects.get(user_name=settings.USER_NAME)
    template = loader.get_template('user.html')
    context = {
        'user' : user_details,
    }
    return HttpResponse(template.render(context,request))


def user_inspect(request,user_name):
    try:
        user_details = models.users.objects.get(user_name=user_name)
    except:
        return redirect('/404/')
    context = {
        'user_details' : user_details,
        'error_message' : 'user not found',
        } 
    template = loader.get_template('user_view.html')
    
    return HttpResponse(template.render(context,request))

def error(request):
    template = loader.get_template('404.html')
    context = {
        'message' : 'user not found'
    }
    return HttpResponse(template.render(context,request))

def product_upload(request):
    template = loader.get_template('upload.html')
    context = {
    }
    return HttpResponse(template.render(context,request))

import random
import string

def product_id_generator(size=10, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    product_id = ''.join(random.choice(chars) for _ in range(size))
    try:
        product = models.Product.objects.get(product_id=product_id)
    except:
        product = None    
    if product == None:
        product_id = product_id
        return product_id
    else:
        product_id_generator()

def product_upload_done(request):
    if request.method == 'POST':
        user_name = models.users.objects.get(user_name=settings.USER_NAME)
        product_name = request.POST.get('product_name')
        product_description = request.POST.get('product_description')
        product_price = request.POST.get('product_price')
        product_image = request.FILES.get('product_image')
        product_id = product_id_generator()
        
        product = models.Product(
            user_name = user_name,
            product_id = product_id,
            product_name = product_name,
            product_description = product_description,
            product_price = product_price,
            current_bid = product_price,
        )
        product_images = models.Product_images(
            product_id = product,
            product_images = product_image,
        )
        product.save()
        product_images.save()
        return redirect('/user/my_products')
    else:
        return HttpResponse('error')    
        
def my_products(request):
    template = loader.get_template('my_products.html')
    products = models.Product.objects.filter(user_name=settings.USER_NAME).all()
    total_set = {}
    for product in products:
        image = models.Product_images.objects.filter(product_id=product.product_id).first()
        total_set[product] = image
    context = {
         'data' : total_set,    
    }
    return HttpResponse(template.render(context,request))

import json
def new_bid(request):
    if request.method == 'POST':
        logged_in = True if settings.LOGGED_IN else False
        if not logged_in:
            return HttpResponseRedirect('/login')
        received_data = json.loads(request.body)
        product_id = models.Product.objects.get(product_id = received_data['product_id'])
        user_name = models.users.objects.get(user_name=settings.USER_NAME)
        bid = received_data['new_amount']
        new_bid = models.bidding(
            product_id = product_id,
            user_name = user_name,
            for_price = int(bid)
        )
        new_bid.save() 
        product = models.Product.objects.get(product_id = received_data['product_id'])
        product.current_bid = int(bid)
        product.num_of_bids +=1
        product.save()
        print("okk")
        return JsonResponse("goog",safe=False)
    else:
        return HttpResponse('error')    




#api
@csrf_exempt
def user_api(request):
    items = models.users.objects.all().values()
    return JsonResponse(list(items), safe=False)

@csrf_exempt
def bids_api(request,auction_name):
    product = models.Product.objects.get(product_id = auction_name)
    bidding = models.bidding.objects.filter(product_id=auction_name).all()[::-1]
    bidding_list = [{'bid_amount': bid.for_price, 'bidder_name': bid.user_name.user_name} for bid in bidding]
    data = {
        'current_bid' : product.current_bid,
        'bid' : bidding_list,
    }
    return JsonResponse(data)