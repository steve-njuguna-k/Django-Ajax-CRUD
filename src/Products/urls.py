from . import views
from django.urls import path

urlpatterns = [
    path('', views.Index, name="Index"),
    path('api/products/', views.ProductsAPI, name="ProductsAPI"),
    path('api/products/add/', views.AddProductAPI, name="AddProductAPI"),
    path('api/products/<int:id>/', views.ProductsDetailsAPI, name="ProductsDetailsAPI"),
    path('api/products/edit/<int:id>/', views.EditProductAPI, name="EditProductAPI"),
    path('api/products/delete/<int:id>/', views.DeleteProductAPI, name="DeleteProductAPI"),
]
