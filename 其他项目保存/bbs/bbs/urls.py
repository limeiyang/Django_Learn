"""bbs URL Configuration

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
from django.conf.urls.static import static
from django.conf import settings

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('post/list/', views.home),
    path('post/create/', views.create_post),
    path('post/read/', views.read_post),
    path('post/comment/', views.comment),
    path('post/delete/', views.post_delete),
    path('post/edit/', views.post_edit),

    path('user/register/', views.register),
    path('user/login/', views.login),
    path('user/logout/', views.logout),
    path('user/info/', views.user_info),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
