from django.contrib import admin
from .models import Category
from django.utils.html import format_html

class CategoryAdmin(admin.ModelAdmin):

    def category_image_tag(self, obj):
         return format_html('<img src="{}" width="90" height="90" />'.format(obj.category_image.url) )

    list_display = ('category_name', 'slug', 'description', 'category_image_tag',)
    prepopulated_fields = {'slug': ('category_name',)}
    category_image_tag.short_description = 'Category image'


admin.site.register(Category, CategoryAdmin)