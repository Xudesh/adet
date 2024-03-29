from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from training.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('training.urls')),
    path('users/', include('users.urls')),
    path('quizes/', include('quizes.urls')),
    path('bizler/', include('bizler.urls'))

] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
