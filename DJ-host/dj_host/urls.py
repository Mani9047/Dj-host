"""
URL configuration for dj_host project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<str:username>/view/', render_uploaded_file, name='render_uploaded_file'),
    path('', home, name='home'),
    path('login/', user_login, name='login'),
    path('logout/',user_logout, name='logout'),
    path('singup/',signup, name='sing'),
    path('file/', files, name='file'),
    path('dashbord/', dash, name='dash'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
