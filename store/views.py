from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *

# Create your views here.
@api_view()
def product_list(request):
    return Response('ok')


@api_view()
def product_detail(request,id):
    try:
        product = Product.objects.get(pk=id)
        serializer = ProductSterializer(product)
        return Response(serializer.data)
    except Product.DoesNotExist:
         return Response(status=404)