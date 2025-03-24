from django.contrib import admin
from django.utils.html import format_html

from django.contrib.auth.admin import UserAdmin
from .models import Account

# Register your models here.

class AccountAdmin(UserAdmin):
   # def image_tag(self, obj):
   #     return format_html('<img src="{}" width="90" height="90" />'.format(obj.user_image.url) )
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_admin', 'is_staff' ,'is_active',) #'image_tag',)
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)
    #image_tag.short_description = 'User image'

        # Disable admin log entries for this model to avoid foreign key issues
    def log_addition(self, request, object, message):
        pass

    def log_change(self, request, object, message):
        pass

    def log_deletion(self, request, object, message):
        pass



    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)
admin.autodiscover()