from django.shortcuts import render # 페이지 호출할 때 쓰는 import
from django.http import HttpResponse # Http자체로 불러갈 수 있는 import
from django.contrib.auth.hashers import make_password # password 암호화 하기위해 django에서 주는 import
from .models import Userinfo # 내가 가져올 class import해주기
# Create your views here.

def index(request):
    users = Userinfo.objects.all()
    return render(request, 'index.html',{"users" : users})

def singup(request):
    if request.method == "POST":
        id = request.POST.get('id',None) # request.POST.get('name값', None일 수 있다.)
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
        user.save() #save()가 데이터를 DB에 집어넣는 코드인듯하다. 
        return render(request, 'register.html')
    else:
        return render(request, 'register.html')
    
    

