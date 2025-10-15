from django.shortcuts import render
from .models import Product
# Create your views here.
def ProductDetail(request, pk):
    product = Product.objects.get(id = pk)
    context = {
        'product':product
    }
    return render(request,'products_detail.html', context)

def ProductList(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request,'products_list.html',context)