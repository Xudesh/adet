from django.urls import path
from .views import *

urlpatterns = [
    path("", view=Base, name='home'),
    path('<slug:subject_slug>/', view=LessonView, name='lessons'),
    path('lesson/<slug:slug>/', view=LessonDetailView, name='lesson_detail'),
    path('subject/', view=subjects_view, name='sub'),
    path('ata-analar/', view=AtaAnalar, name='parents')
]
