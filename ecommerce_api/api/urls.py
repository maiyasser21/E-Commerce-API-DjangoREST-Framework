from django.urls import path
from api.views import CategoryList, CategoryDetail, ProductList, ProductDetail, UserDetail, OrderListCreate

urlpatterns = [
    path('categories/', CategoryList.as_view()),
    path('categories/<int:pk>/', CategoryDetail.as_view()),
    path('products/', ProductList.as_view()),
    path('products/<int:pk>/', ProductDetail.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('orders/', OrderListCreate.as_view()),
    
]
