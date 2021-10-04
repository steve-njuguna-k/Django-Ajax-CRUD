from django.shortcuts import render
from .models import Products
from .serializers import PropertySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

def Index(request):
    return render(request, 'Index.html')

@api_view(['GET'])
def ProductsAPI(request):
    products = Products.objects.all()
    serializer = PropertySerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def ProductsDetailsAPI(request, id):
    product = Products.objects.get(id=id)
    serializer = PropertySerializer(product, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def AddProductAPI(request):
    serializer = PropertySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def EditProductAPI(request, id):
    product = Products.objects.get(id=id)
    serializer = PropertySerializer(instance=product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_304_NOT_MODIFIED)

@api_view(['DELETE'])
def DeleteProductAPI(request, id):
    if request.is_ajax():
        product = Products.objects.get(id=id)
        product.delete()
        return Response('Product successfully Deleted!', status=status.HTTP_200_OK)

    return Response("That Product Doesn't Exists!", status=status.HTTP_204_NO_CONTENT)