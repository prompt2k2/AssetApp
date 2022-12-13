from django.contrib import admin
from .models import Items
# Register your models here.


@admin.register(Items)
class Product(admin.ModelAdmin):
    list_display = ('name', 'item_number', 'product')