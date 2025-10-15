from django.shortcuts import render
# from products.models import Product

# Create your views here.
def admin_home(request):
    # product = Product.objects.all()
    return render (request,'admin.html')