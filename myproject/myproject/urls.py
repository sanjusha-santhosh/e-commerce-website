"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('myapp.urls')),
    path('user/',include('myapp.urls')),
    path('main/',include('myapp.urls')),
    path('mobile/', include('myapp.urls')),
    path('fash/', include('myapp.urls')),
    path('lap/', include('myapp.urls')),
    path('buy/', include('myapp.urls')),
    path('cart/', include('myapp.urls')),
    path('ofr/', include('myapp.urls')),
    path('iphn/', include('myapp.urls')),
    path('oppo/', include('myapp.urls')),
    path('sam/', include('myapp.urls')),
    path('mi/', include('myapp.urls')),
    path('women/', include('myapp.urls')),
    path('saree/', include('myapp.urls')),
    path('kurt/', include('myapp.urls')),
    path('west/', include('myapp.urls')),
    path('men/', include('myapp.urls')),
    path('kids/', include('myapp.urls')),
    path('wat/', include('myapp.urls')),
    path('hd/', include('myapp.urls')),
    path('ear/', include('myapp.urls')),
    path('tv/', include('myapp.urls')),
    path('rf/', include('myapp.urls')),
    path('head/', include('myapp.urls')),
    path('add/', include('myapp.urls')),
    path('add2/', include('myapp.urls')),
    path('buy2/', include('myapp.urls'))

]
