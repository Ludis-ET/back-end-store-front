from django.shortcuts import render
from store.models import Product
from django.db.models import Q,F
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    # try:
    #     query_set = Product.objects.get(pk=0)
    # except ObjectDoesNotExist:
    #     pass
    # list(query_set)
    query_set = Product.objects.order_by('-title')

    return render(request,'index.html',{'products':list(query_set)})