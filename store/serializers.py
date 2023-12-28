from rest_framework import serializers
from .models import *
from decimal import Decimal




class ProductSterializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    unit_price = serializers.DecimalField(max_digits=6,decimal_places=2)
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    collection = serializers.StringRelatedField()

    def calculate_tax(self,product: Product):
        return product.unit_price * Decimal(1.1)