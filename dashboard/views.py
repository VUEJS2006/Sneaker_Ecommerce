from django.shortcuts import render
# from products.models import Product, Category

# Create your views here.
def admin_home(request):
    # product = Product.objects.all()
    return render (request,'admin.html')

def CategoryList(request):
    return render(request, 'admincategory.html')