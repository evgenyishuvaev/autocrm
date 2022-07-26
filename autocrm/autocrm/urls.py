from django.contrib import admin
from django.urls import path, include, re_path

from django.views.static import serve

from .settings import DEBUG, STATIC_ROOT



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
else:
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', serve, {
            'document_root': STATIC_ROOT,
        }),
    ]