from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Category,Product,Order

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','first_name','last_name']
        
class OrderSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    products=ProductSerializer(many=True)
    
    class Meta:
        model=Order
        fields='__all__'
