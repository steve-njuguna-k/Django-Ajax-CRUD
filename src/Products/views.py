from django.shortcuts import render
from .models import Products
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

def Index(request):
    return render(request, 'Index.html')

@api_view(['GET'])
def ProductsAPI(request):
    products = Products.objects.all().order_by('id')
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def ProductsDetailsAPI(request, id):
    product = get_object_or_404(Products, id=id)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def AddProductAPI(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def EditProductAPI(request, id):
    product = get_object_or_404(Products, id=id)
    serializer = ProductSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    print(request.data)
    return Response(serializer.errors, status=status.HTTP_304_NOT_MODIFIED)

@api_view(['DELETE'])
def DeleteProductAPI(request, id):
    if request.is_ajax():
        product = get_object_or_404(Products, id=id)
        product.delete()
        return Response('Product successfully Deleted!', status=status.HTTP_200_OK)

    return Response("That Product Doesn't Exists!", status=status.HTTP_204_NO_CONTENT)