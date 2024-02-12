"""
URL configuration for myproject project.

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
from django.urls import path, include
from homepage import views
from myproject import settings
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from .views import ModelViewSet

router = DefaultRouter()
router.register(r'your_model', ModelViewSet)


urlpatterns = [
    path('check_duplicate_id/', views.check_duplicate_id),
    path('regist/', views.signup, name='signup'),
    path('accounts/', include('allauth.urls')),
    path('', include('social_django.urls', namespace='social')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.main, name='main'),
    path('send_code_email/', views.send_code_email),
    path('verify_code/', views.verify_code),
    path('login/', views.login, name='login'),
    path('api/', include(router.urls)),
    
]
