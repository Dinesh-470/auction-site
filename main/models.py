from django.db import models

# Create your models here.
class users(models.Model):
    user_name = models.CharField(max_length=20)
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    number = models.CharField(max_length=15)
    image = models.ImageField(upload_to='user_images/')
    def __str__(self) -> str:
        return self.user_name
    
        