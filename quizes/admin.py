from django.contrib import admin
from .models import *


class AnswerAdmin(admin.StackedInline): 
    model = Answer 
    
class QuestionAdmin(admin.ModelAdmin): 
    inlines = [AnswerAdmin] 
    list_display = ['text', 'language']
    list_display_links = ['text', 'language']



admin.site.register(Question, QuestionAdmin) 
admin.site.register(Answer) 

admin.site.register(TestResult)
admin.site.register(TestResultDetail)