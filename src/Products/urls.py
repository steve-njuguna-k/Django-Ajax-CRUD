from . import views
from django.urls import path

urlpatterns = [
    path('', views.Index, name="Index"),
    path('add/', views.AddProducts, name="AddProducts")
]
