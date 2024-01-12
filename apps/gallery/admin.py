from django.contrib import admin
from .models import Gallery
from django.utils.html import format_html
# Register your models here.

class GalleryAdmin(admin.ModelAdmin):

    def gallery_image_tag(self, obj):
        return format_html('<img src="{}" width="90" height="90" />'.format(obj.gallery_image.url) )

    list_display = ('name', 'slug', 'description', 'gallery_image_tag',)
    prepopulated_fields = {'slug': ('name',)}
    gallery_image_tag.short_description = 'Gallery image'


admin.site.register(Gallery, GalleryAdmin)