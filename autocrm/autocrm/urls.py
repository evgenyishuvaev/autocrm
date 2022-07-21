from django.contrib import admin
from django.urls import path, include

from .settings import DEBUG



rest_api_patterns = [
    path('', include('car_accounting.api_urls'))# car_accounting api's
]


urlpatterns = [

    path('', include('car_accounting.urls')),
    path('admin/', admin.site.urls, name='admin_panel'),

    path('accounts/', include('accounts.urls')),
    path('', include('accounts.api_urls')),

    path('api/v1/', include(rest_api_patterns))
]

if DEBUG:

    urlpatterns = [
        path('__debug__/', include('debug_toolbar.urls')),
    ] + urlpatterns
