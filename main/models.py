from django.db import models

# Create your models here.
class User(models.Model):
   user_name = models.CharField(max_length=20)
   full_name = models.CharField(max_length=50)
   email = models.EmailField(max_length=254)
   mobile_number = models.TextField()
   password = models.TextField()

   
class user_images(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    user_image = models.ImageField('/media',None)
