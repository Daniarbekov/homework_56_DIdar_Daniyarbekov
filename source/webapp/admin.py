from django.contrib import admin
from webapp.models import Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','description','category','image','balance','price')
    list_filter = ('id','name','description','category','image','balance','price')
    fields = ('id','name','description','category','image','balance','price')
    readonly_fields = ('id','category')

admin.site.register(Product, ProductAdmin)