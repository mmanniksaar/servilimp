from django.contrib import admin
from .models import Client
from django.utils.html import format_html
# Register your models here.

class ClientsAdmin(admin.ModelAdmin):

    def client_image_tag(self, obj):
        return format_html('<img src="{}" width="90" height="90" />'.format(obj.client_image.url) )

    list_display = ('client_name', 'client_slug', 'client_image_tag',)
    prepopulated_fields = {'client_slug': ('client_name',)}
    client_image_tag.short_description = 'Client image'


admin.site.register(Client, ClientsAdmin)