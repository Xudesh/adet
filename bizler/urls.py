from django.urls import path
from .views import *

urlpatterns = [
    path('ata-analar/', view=AtaAnalar, name='parents'),
    path('teachers/', view=teachers, name='teachers')
]
