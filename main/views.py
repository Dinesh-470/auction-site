from django.shortcuts import redirect
from django.template import loader
from django.http import HttpResponse
from . import models
from django.conf import settings
# Create your views here.
def index(request):
    logged_in = True if settings.LOGGED_IN else False
    
    template = loader.get_template('index.html')
    context = {
        'login' : logged_in,
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
        user = models.users.objects.get(user_name=user_name)
        if password == user.password:
            settings.LOGGED_IN =True
            settings.USER_NAME = user.user_name
            return redirect('/')
        else:
           return HttpResponse('user not found or password wrong.')
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
    data = models.Product.objects.all()
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
    bidding = models.bidding.objects.filter(product_id=auction_name).all()

    template = loader.get_template('auction.html')
    context = {
        'product_id':auction_name,
        'data' : data,
        'image' : image,
        'activity' : bidding,
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