"""CPAS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from . import views
from . views import *

urlpatterns = [

    
    path('', views.start,name="start"),
    path('home', views.home,name="home"),
    path('profile/<int:pk>',ProfileView.as_view(),name="profile"),
    path('register',views.registerPage,name="register"),
    path('login',views.loginPage,name="login"),
    path('setup',views.setup,name="setup"),
    path('logout',views.logoutUser,name="logout"),
    path('safetyguide',views.safetyguide,name="safetyguide"),
    path('assist',views.assist,name="assist"),
    path('predictor',views.predictor,name="predictor"),
    path('predictorresult',views.predictorresult,name="predictorresult"),


    




]
