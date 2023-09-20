from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class basemodel(models.Model):
    uid=models.UUIDField(default=uuid.uuid4,editable=False,primary_key=True)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now_add=True)
    
    class Meta:
        abstract=True
        
class pizzacat(basemodel):
    catname=models.CharField(max_length=100)
    
    
class pizza(basemodel):
    category=models.ForeignKey(pizzacat,on_delete=models.CASCADE,related_name="pizzas")
    pizza_name=models.CharField(max_length=100)
    price=models.IntegerField(default=100) 
    images=models.ImageField(upload_to='images',default=None)
    
class cart(basemodel):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,related_name="carts",null=True)
    is_paid=models.BooleanField(default=False)
class cartitems(basemodel):
    pizza=models.ForeignKey(pizza,on_delete=models.CASCADE)
    cart=models.ForeignKey(cart,on_delete=models.CASCADE,related_name="cart_items")

    
