"""demo URL Configuration

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
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from joke import views

urlpatterns = [
    path('admin/', admin.site.urls),
	path('joke/index',views.index),
	path('home/',views.home),
    path('homesql/',views.homesql),
    path('form_test/', views.form_test),
    path('user/info/', views.user_info),

]
# 添加本地图片的配置
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)