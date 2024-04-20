from django.contrib import admin
from . import models
# Register your models here.
class user_view(admin.AdminSite):
    list_display = ['user_name','email','image']
    
admin.site.register(models.users)
admin.site.register(models.Product)
admin.site.register(models.Product_images)
admin.site.register(models.bidding)
admin.site.register(models.user_activity)