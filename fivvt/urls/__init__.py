from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView

API_PREFIX = 'api'


urlpatterns = [
    path('admin/', admin.site.urls),
    path(f'{API_PREFIX}/v0/', include('fivvt.urls.v0')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__', include(debug_toolbar.urls)),
        path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
        path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger')
    ]
