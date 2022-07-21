from django.contrib import admin
from django.urls import path, include
from .settings import DEBUG


urlpatterns = [

    path('', include('car_accounting.urls')),
    path('admin/', admin.site.urls, name='admin_panel'),
    path('accounts/', include('accounts.urls')),
    
]

if DEBUG:

    urlpatterns = [
        path('__debug__/', include('debug_toolbar.urls')),
    ] + urlpatterns
