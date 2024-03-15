from django.urls import path
from .views import *


urlpatterns = [
    path('sign_up/', view=sign_up, name='sign_up'),
    path('sign_in/', view=sign_in, name='sign_in'),
    path('edit-profile/', view=edit_profile, name='edit'),

    path('sign_out/', view=sign_out, name='sign_out'),
    path('profile/', user_daily_visits, name='profile'),
]
