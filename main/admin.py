from django.contrib import admin
from .models import user_images,User
# Register your models here.


class user_details(admin.ModelAdmin):
    list_display = ["user_name","email"]
    
class user_image(admin.ModelAdmin):
    list_display = ("user_name","user_image")
        
admin.site.register(User,user_details)
admin.site.register(user_images,user_image)
