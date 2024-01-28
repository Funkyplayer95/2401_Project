from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password # password 암호화 하기위해 django에서 주는 import
from .models import Userinfo,Userimage # 내가 가져올 class import해주기
# Create your views here.
@csrf_exempt
def check_duplicate_id(request):
    userid = request.POST.get('userid', None)
    user = Userinfo.objects.filter(user_id=userid)
    if user.exists():
        return JsonResponse({'status': 'error', 'message': '중복된 ID가 있습니다.'}, safe=False)
    else:
        return JsonResponse({'status': 'success', 'message': '사용 가능한 ID입니다.'}, safe=False)

def singup(request):
    if request.method == "POST":
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
        
        duplicate_check_result = check_duplicate_id(request)

        if 'status' in duplicate_check_result and duplicate_check_result['status'] == 'error':
            # 중복된 ID 처리 (예: 경고 메시지 출력)
            return render(request, 'register.html', {'error_message': duplicate_check_result['message']})
        else:
            # 중복이 아닌 경우 계속 진행
            userid = request.POST.get('userid',None)
            user = Userinfo(user_id=userid,
                            user_password=make_password(password),
                            user_name=name,
                            user_gender=gender,
                            user_rrn1=rrn1,
                            user_rrn2=rrn2,
                            user_email=email1 + "@" + email2,
                            user_address_num=address_num,
                            user_address_doro=address_doro,
                            user_address_jibun=address_jibun,
                            user_address_detail=address_detail,)
                            # user_image_id=img
            
            user.save() # django 에서 db에 저장하는 기능인것같다.
            
            return render(request, 'register.html')

    else:
        # GET 요청인 경우
        return render(request, 'register.html')