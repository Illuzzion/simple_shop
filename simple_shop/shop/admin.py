from django.contrib import admin

from .models import Product, Category, ProductAdditionalImage, ProductPrice, ProductMeasure


class ProductImageInline(admin.TabularInline):
    model = ProductAdditionalImage
    extra = 0


class ProductPriceInline(admin.TabularInline):
    model = ProductPrice
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'created', 'updated']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('available',)
    inlines = [ProductImageInline, ProductPriceInline]


# @admin.register(Category)
# class ProductCategoryAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ('name',)}


admin.site.register(ProductMeasure)
