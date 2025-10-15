from django.urls import path
from . import views

urlpatterns = [
    path('productdetail/<int:pk>', views.ProductDetail, name='productdetail'),
    path('productlist/', views.ProductList, name='productlist'),

]