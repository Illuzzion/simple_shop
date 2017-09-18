from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import Category


@admin.register(Category)
class ProductCategoryAdmin(DraggableMPTTAdmin):
    prepopulated_fields = {'slug': ('name',)}
    mptt_level_indent = 20
    list_display = ('tree_actions', 'indented_title')
    list_display_links = ('indented_title',)
