from django.contrib import admin
from .models import *

class ParentsAdmin(admin.ModelAdmin):
    list_display = ['title', 'public_date']


admin.site.register(Parents, ParentsAdmin)