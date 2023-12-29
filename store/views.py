from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *


# Create your views here.
@api_view(['GET','POST'])
def product_list(request):
    if request.method == 'GET':
        queryset = Product.objects.select_related('collection').all()
        serializer = ProductSterializer(queryset,many=True,context={'request':request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSterializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    

@api_view(['GET','PUT','DELETE'])
def product_detail(request,id): 
    product = get_object_or_404(Product,pk=id)
    if request.method == 'GET':
        serializer = ProductSterializer(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSterializer(product,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        if product.orderitem_set.count() > 0:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view()
def collection_detail(request,id): 
    product = get_object_or_404(Collection,pk=id)
    serializer = ProductSterializer(product)
    return Response(serializer.data)