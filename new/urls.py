
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.i18n import set_language
from django.conf import settings
from django.conf.urls.static import static

from blog.admin_views import custom_admin_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls')),
    path('i18n/', set_language, name='set_language'),
    path('admin/logout/', custom_admin_login, name="custom-admin-login"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
