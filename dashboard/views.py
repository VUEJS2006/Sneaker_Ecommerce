from django.shortcuts import render, redirect
from products.models import Product, Category

# Create your views here.
def admin_home(request):
    # product = Product.objects.all()
    return render (request,'admin.html')

def CategoryList(request):
    categories = Category.objects.all()
    context = {
        'categories':categories
    }
    return render(request, 'admincategory.html',context)
def CategoryCreate(request):
    if request.method == "POST":
        category= Category.objects.create(
            name = request.POST.get('name'),
        )
        category.save()
        return redirect('/dashboard/admincategory/')
def CategoryUpdate(request, pk):
    category  = Category.objects.get(id = pk)
    if request.method == "POST":
        category.name = request.POST.get('name')
        category.save()
        return redirect('/dashboard/admincategory/')
def CategoryDelete(request, pk):
    category = Category.objects.get(id = pk)
    if request.method == "POST":
       category.delete()
       return redirect('/dashboard/admincategory/')
def ProductList(request):
    products = Product.objects.all()
    categorise = Category.objects.all()
    context = {
        'products':products,
        'categorise':categorise
    }
    return render(request, 'adminproduct.html', context)
def ProductCreate(request):
    if request.method == "POST":
        product = Product.objects.create(
            name = request.POST['name'],
            # name = request.POST.get('name'),
            price = request.POST['price'],
            category_id  = request.POST['category'],
            desciption = request.POST['desciption'],
            image = request.FILES.get('image'),
            is_sale = request.POST['is_sale'] == "on",
            sale_price = request.POST['sale_price']
        )
        product.save()
        return redirect('/dashboard/adminproduct/')



    