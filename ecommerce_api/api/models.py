from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ManyToManyField(Product)
    date_created=models.DateTimeField(auto_now_add=True)
    @property
    def products(self):
        return self.product.count()
    @property
    def price(self):
        total=0
        for p in self.product.all():
            total+=p.price
        return total*self.products
    
    
    def __str__(self):
        return f"{self.user}"
    
    
