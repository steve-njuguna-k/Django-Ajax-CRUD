from django.shortcuts import render
from .models import Products
from django.http import JsonResponse

# Create your views here.
def Index(request):
    products = Products.objects.all()
    return render(request, 'Index.html', {"products":products})

def AddProducts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        category = request.POST.get('category')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')

        obj = Products.objects.create(name=name, category=category, quantity=quantity, price=price)

        product = {
            "id": obj.name,
            "name": obj.category,
            "category": obj.category,
            "quantity": obj.quantity,
            "price": obj.price,
        }

        data = {
            "product":product
        }

    return JsonResponse(data)