from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny

from django.conf import settings       # static fayllarni , media fayllarni olishga kerak
from django.conf.urls.static import static    # static fayllarni , media fayllarni olishga kerak


schema_view = get_schema_view(
    openapi.Info(
        title="Farm Application Rest API",
        default_version="v1",
        description="Swagger docs for Rest API",
        contact=openapi.Contact(email="elmurodzulfiqarov@gmail.com"),
    ),
    public=True,
    permission_classes=(AllowAny, )
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('accounts.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name="swagger-docs"),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name="redoc-docs")

]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)