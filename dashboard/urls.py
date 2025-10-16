from django.urls import path
from . import views 

urlpatterns = [
    path('dashboard/', views.admin_home, name='dashboard'),
    path('admincategory/', views.CategoryList, name='admincategory'),
]