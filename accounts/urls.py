"""
URL configuration for dota2boosting project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from .views import *

urlpatterns = [
    path("login/", UserLoginView.as_view(), name = "userlogin"),
    path("users/", UserView.as_view(), name = "users"),
    path("register/", UserRegisterView.as_view(), name = "userregister"),
    path("users/<int:pk>/", UserRetrieveUpdateDestroyView.as_view(), name = "userretupddel"),
]
