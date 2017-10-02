from django.contrib import admin

from .models import Product, ProductAdditionalImage, ProductPrice, ProductMeasure


class ProductImageInline(admin.TabularInline):
    model = ProductAdditionalImage
    extra = 0


class ProductPriceInline(admin.TabularInline):
    model = ProductPrice
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['showimg', 'name', 'category', 'updated', 'available']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('available',)
    inlines = [ProductImageInline, ProductPriceInline]


admin.site.register(ProductMeasure)
