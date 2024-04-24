from django.db import models

# Create your models here.
class users(models.Model):
    user_name = models.CharField(max_length=20,primary_key=True)
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    number = models.CharField(max_length=15,unique=True)
    image = models.ImageField(upload_to='user_images/')
    password = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.user_name
    
class Product(models.Model):
    user_name = models.ForeignKey(users,on_delete=models.CASCADE)
    product_id = models.CharField(max_length=30,primary_key=True)
    product_name = models.TextField()
    product_description = models.TextField(default=None,null=True)
    product_price = models.IntegerField()
    current_bid = models.IntegerField()
    num_of_bids = models.IntegerField(default=0)
    def __str__(self) -> str:
        return self.product_id
    
class Product_images(models.Model):
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    product_images = models.ImageField(upload_to='product_images/')
    def __str__(self) -> str:
        return self.product_id.product_id
    
class bidding(models.Model):
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    user_name = models.ForeignKey(users,on_delete=models.CASCADE)
    for_price = models.IntegerField()
    def __str__(self) -> str:
        return f'{self.user_name.user_name} bidded for {self.product_id.product_id}'
    
class user_activity(models.Model):
    user_name = models.ForeignKey(users,on_delete=models.CASCADE)
    activity = models.TextField()
    def __str__(self) -> str:
        return self.activity      