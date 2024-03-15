from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'get_html_photo']
    list_display_links = ['user', 'get_html_photo']


    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=30px /")
        
    get_html_photo.short_description = 'Sureti'


admin.site.register(Profile, ProfileAdmin)

