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
from django.contrib import admin
from django.urls import path, include
# http://127.0.0.1/
# http://127.0.0.1/app/

# http://127.0.0.1/create/
# http://127.0.0.1/read/1/
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('myapp.urls'))
]

# django 실행방법.
# django-admin startproject 프로젝트이름 . (.은 해당위치에 설치하겠다는 표시)
# python3 manage.py runserver -> 서버 실행 127.0.0.1:8000 기본
# django-admin startapp 앱이름 (경로에 앱이름으로된 파일 생성)
# 프로젝트에 있는 urls 설정 변경 후 (지금 진행함.)
# 해당 파일을 만든 앱폴더에 복사
# 복사한 app폴더 안 urls 코드 수정.
# views.py 폴더 안에 HttpResponse 추가 import하고
# 원하는 함수를 만들어서 진행.
# 앱안에있는 urls에 views import하고, path 경로 지정하여 추가.

#즉, 사용자가 서버에 접속하면
#프로젝트에 있는 urls에서 반응하여 app으로 이동
#app urls에 지정돼있는 경로따라 views 호출
# views에서 해당 함수를 불러와서 진행.\

#여기까지가 라우팅에 대한 이론.
# 힘내보자.