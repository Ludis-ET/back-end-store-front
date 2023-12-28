from django.contrib import admin
from .models import *

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','unit_price','inventory_status']
    list_editable = ['unit_price']
    list_per_page = 30

    @admin.display(ordering='inventory')
    def inventory_status(self,Product):
        return 'High' if Product.inventory < 10 else 'Low'

admin.site.register(Collection)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','membership']
    list_editable = ['membership']
    ordering = ['first_name','last_name']
    list_per_page = 10