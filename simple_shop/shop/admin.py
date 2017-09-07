from django.contrib import admin

from .models import Product, Category


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'created', 'updated']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['price']
    list_filter = ('available',)


class ProductCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, ProductCategoryAdmin)
