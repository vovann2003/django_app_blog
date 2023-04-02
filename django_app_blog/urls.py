"""django_app_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from rest_framework import permissions
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title='Snippets API',
        default_version='v1',
        description='This is an api for uploading recipes and viewing them',
        contact=openapi.Contact(email='vovanlebedev38@gmail.com'),
        license=openapi.License(name='BSD Licence')
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)


urlpatterns = [
  path('admin/', admin.site.urls),
  path('', include('app_blog.urls')),
  path('api/', include('app_blog_api.urls')),
  path('i18n/', include('django.conf.urls.i18n')),
  re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),  # The CKEditor path
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
