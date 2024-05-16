from django.urls import path
from .views import *

urlpatterns = [
    path('all/', view=quize_all, name='quizes'),
    path('<slug:subject_slug>/test/', view=test_view, name='test'),
    path('result/<int:test_result_id>/', view=test_result, name='results'),
    path('<slug:slug>/tests/', view=pass_test, name='pass_test')
]