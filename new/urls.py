
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.i18n import set_language




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls')),
    path('i18n/', set_language, name='set_language'),
]
