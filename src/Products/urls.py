from . import views
from django.urls import path

urlpatterns = [
    path('', views.Index, name="Index"),
    path('add/', views.AddProducts, name="AddProducts"),
    path('edit/', views.UpdateProduct, name="UpdateProduct"),
    path('delete/', views.DeleteProduct, name="DeleteProduct"),
]
