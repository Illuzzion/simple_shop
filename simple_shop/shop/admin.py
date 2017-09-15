from django.contrib import admin

from .models import Product, Category, ProductAdditionalImage, ProductPrice, ProductMeasure


class ProductImageInline(admin.TabularInline):
    model = ProductAdditionalImage
    extra = 0


class ProductPriceInline(admin.TabularInline):
    model = ProductPrice
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'created', 'updated']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('available',)
    inlines = [ProductImageInline, ProductPriceInline]


class ProductCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, ProductCategoryAdmin)
admin.site.register(ProductMeasure)
