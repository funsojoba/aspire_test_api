from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework import permissions
from django.contrib import admin
from django.urls import path, include


schema_view = get_schema_view(
    openapi.Info(
        title="LOTR Characters API",
        default_version='v1',
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('API.urls')),
    path('swagger', schema_view.with_ui('swagger',
                                        cache_timeout=0), name='schema-swagger-ui'),
]
