from django.contrib import admin
from .models import users
# Register your models here.
class user_view(admin.AdminSite):
    list_display = ['user_name','email','image']
    
admin.site.register(users)