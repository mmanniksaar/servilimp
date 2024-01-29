from django.contrib import admin
from .models import About
from django.utils.html import format_html

class AboutAdmin(admin.ModelAdmin):

    list_display = ('custom_row_view',)

    def custom_row_view(self, obj):
        # Siin saad luua oma kohandatud HTML-koodi reavaateks
        return format_html(
            '<div style="background-color: #f0f0f0; line-height: 2; font-size: 22px; padding: 30px; text-align: justify;">'
            '<strong>{}</strong><br><br><br>'
            '{}<br><br><br>{}<br><br><br>{}<br><br><br>{}'
            '</div>',
            obj.first_txt, obj.second_txt, obj.third_txt, obj.fourth_txt, obj.fifth_txt
        )

    custom_row_view.short_description = 'About View'

"""     def has_add_permission(self, request):
        # Keelame "Add" nupu
        return False """
    
admin.site.register(About, AboutAdmin)