from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from .models import Userinfo
# Create your views here.
# 여기에 함수 및 다양한 

def index(request):
    users = Userinfo.objects.all()
    return render(request, 'index.html',{"users" : users})

def singup(request):
    if request.method == "POST":
        id = request.POST.get('id',None)
        password = request.POST.get('password',None)
        name = request.POST.get('name',None)
        gender = request.POST.get('gender',None)
        rrn1 = request.POST.get('jumin1',None)
        rrn2 = request.POST.get('jumin2',None)
        email1 = request.POST.get('emailId',None)
        email2 = request.POST.get('domain-txt',None)
        address_num = request.POST.get('address_num',None)
        address_doro = request.POST.get('address_doro',None)
        address_jibun = request.POST.get('address_jibun',None)
        address_detail = request.POST.get('address_detail',None)
        img = request.POST.get('imgfile',None)

        user = Userinfo(user_id=id, user_password=make_password(password),
                        user_name=name, user_gender=gender,
                        user_rrn1=rrn1, user_rrn2=rrn2, user_email=email1+"@"+email2,
                        user_address_num=address_num, user_address_doro=address_doro,
                        user_address_jibun=address_jibun, user_address_detail=address_detail,
                        user_img=img)
        user.save()
        return render(request, 'register.html')
    else:
        return render(request, 'register.html')
    
    

