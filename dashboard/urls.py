from django.urls import path
from . import views 

urlpatterns = [
    path('dashboard/', views.admin_home, name='dashboard'),
    path('admincategory/', views.CategoryList, name='admincategory'),
    path('admincategory/create/', views.CategoryCreate, name='admincategorycreate'),
    path('admincategory/update/<int:pk>', views.CategoryUpdate, name='admincategoryupdate'),
    path('admincategory/delete/<int:pk>', views.CategoryDelete, name='admincategorydelete'),

    path('adminproduct/', views.ProductList, name='adminproduct'),
    path('adminproduct/create/', views.ProductCreate, name='adminproductcreate'),
    

    

]