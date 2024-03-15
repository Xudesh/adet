from django.contrib import admin
from .models import *



class LessonAdmin(admin.ModelAdmin):
    list_display = ['name', 'language', 'date', 'klass']

    list_display_links = ['name', 'language', 'date', 'klass']

    prepopulated_fields = {
        'slug': ['name']
    }


    list_filter = ['language']

    search_fields = ['name', 'klass']



class LanguageAdmin(admin.ModelAdmin):
    list_display = ['subject', 'klass']

    prepopulated_fields = {
        'subject_slug': ['subject']
    }



admin.site.register(Lesson, LessonAdmin)
admin.site.register(Language, LanguageAdmin)




admin.site.index_title = 'Adet'
admin.site.site_title = 'Admin'

admin.site.site_header = "Adet administraciyasi"

