from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

api_v1_urlpatterns: list = [
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('favorites/', include(('favorites.urls', 'favorites'), namespace='favorites')),
    path(
        'notifications/',
        include(
            ('notifications.urls', 'notifications'),
            namespace='notifications')
    ),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='api_v1:schema'),
         name='swagger-ui'),
]

urlpatterns: list = [
    path('api/v1/', include((api_v1_urlpatterns, 'api_v1'))),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
