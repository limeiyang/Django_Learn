"""mgr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from app import views
from django.conf.urls.static import static
from django.views.static import serve
from mgr.settings import MEDIA_ROOT
from django.conf import settings
from django.conf.urls import url
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.login),
    path('regist/',views.regist),
    path('userList/',views.userList),
    path('userDetail/',views.userDetail),
    path('user_delete/',views.user_delete),
    # path('user_update/',views.user_update)
    url(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
    path('checkCode/',views.get_code),
    path('user_update/',views.user_update)
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

