"""
URL configuration for firstprog project.

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
from django.urls import include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index),
    path('shop/',views.shop),
    path('about/',views.about),
    path('contact/',views.contact),
    path('cart/',views.cart),
    path('thankyou/',views.thankyou),
    path('checkout/',views.checkout),
    path('blog/',views.blog),
    path('services/',views.services),
    path('login/',views.login),
    path('data/',views.data),
]

