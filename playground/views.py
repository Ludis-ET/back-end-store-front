from django.shortcuts import render
from store.models import Product


def index(request):
    query_set = Product.objects.all()
    list(query_set)
    
    return render(request,'index.html')