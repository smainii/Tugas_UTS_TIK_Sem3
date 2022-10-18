"""pembelajaranmtk URL Configuration

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
from django.contrib import admin
from django.urls import path
from artikel.views import pemb1
from contoh.views import pemb2
from latihan.views import pemb3
from materi.views import pemb4
from video.views import pemb5

urlpatterns = [
    path('admin/', admin.site.urls),
    path('artikel/', pemb1),
    path('contoh/', pemb2),
    path('latihan/', pemb3),
    path('materi/', pemb4),
    path('video/', pemb5),
]
