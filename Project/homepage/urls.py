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
# from rest_framework.routers import DefaultRouter
# from .views import ModelViewSet

# router = DefaultRouter()
# router.register(r'Userinfo', ModelViewSet)


urlpatterns = [
    path('check_duplicate_id/', views.check_duplicate_id), # 아이디 중복체크
    path('regist/', views.signup, name='signup'), #회원가입
    path('accounts/', include('allauth.urls')), 
    path('', include('social_django.urls', namespace='social')), # 소셜로그인
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), #로그아웃
    path('', views.main, name='main'), # 메인 (날씨,지도)
    path('send_code_email/', views.send_code_email), # 이메일전송
    path('verify_code/', views.verify_code), # 인증코드
    path('login/', views.login, name='login'), #로그인
    # path('api/', include(router.urls)),
    
]
