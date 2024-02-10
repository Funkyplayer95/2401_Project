from django.shortcuts import render, redirect # render = 불러오기 / redirect = 다시 재실행하는
from django.http import JsonResponse, HttpResponse # Json값으로 response하는것 (키 : 벨류)
from django.views.decorators.csrf import csrf_exempt # csrf 충돌을 막기위함이라함. 공부할 것.
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password # password 암호화 하기위해 django에서 주는 import
from django.contrib.auth import login as auth_login
from .models import Userinfo,Cityweather # 내가 가져올 class import해주기
from django.conf import settings # settings.py 참고 가져오기위해.
import requests
import json
import random #랜덤인증코드 전송을 위해
import smtplib #이메일 전송 위해
from email.mime.text import MIMEText #이메일 전송 위해

# Create your views here.

# 장바구니
def cart(request):
    carts = Userinfo.objects.get(user_id = request.user.user_id).carts.all()
    return render(request, 'mypage.html', {'carts':carts})

# 메인
def main(request):
    kakaoapi = settings.KAKAO_API_KEY # settings에 저장되어있는 kakao api key 호출

    #날씨정보 포함 openweathermap API 사용
    openweathermapKey = settings.OPENWEATHERMAP_API_KEY # settings에 저장되어있는 openweathermap api key 호출
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&lang={}&units={}&appid={}'
    cities = Cityweather.objects.all() #return all the cities in the database
    weather_data = []
    for city in cities:
        city_name = city.city_name  # 도시 이름을 가져옵니다.
        city_weather = requests.get(url.format(city_name, 'ko', 'metric', openweathermapKey)).json()
        
        if 'main' in city_weather:
            weather = { #필요한 데이터를 모을 집합체
                'city' : city_name,
                'temperature' : city_weather['main']['temp'],
                'description' : city_weather['weather'][0]['description'],
                'icon' : city_weather['weather'][0]['icon']
            }
            weather_data.append(weather)
        else:
            # 콘솔에 어느 도시의 정보를 불러오는게 실패하는지 확인하기
            print(f"{city_name}의 날씨 정보를 불러오는데 실패했습니다.")

    # 날씨 api 와 카카오지도 api키를 가져와서 context안에 저장시킴.
    context = {'weather_data' : weather_data , 'kakaoapi' : kakaoapi} # context안에 작성하면 html에서 {{ }} 로 불러올 수 있음

    return render(request, 'main.html', context) 

# 아이디 중복 체크
@csrf_exempt
def check_duplicate_id(request):
    userid = request.POST.get('userid', None)
    user = Userinfo.objects.filter(user_id=userid)
    if user.exists():
        # DB에 동일 값이 있을 경우
        return JsonResponse({'status': 'error', 'message': '중복된 ID가 있습니다.'}, safe=False)
    else:
        # DB에 동일 값이 없을 경우
        return JsonResponse({'status': 'success', 'message': '사용 가능한 ID입니다!'}, safe=False)

# 회원가입 DB연동 , Submit하여 제출할때 동작하는 코드 / name의 값을 받아온다
def signup(request):
    if request.method == "POST":
        password = request.POST.get('password',None)
        name = request.POST.get('name',None)
        gender = request.POST.get('gender',None)
        rrn1 = request.POST.get('joomin1',None)
        rrn2 = request.POST.get('joomin2',None)
        email1 = request.POST.get('emailId',None)
        email2 = request.POST.get('domain-txt',None)
        # email3 = request.POST.get('domain-list','')
        address_num = request.POST.get('address_num',None)
        address_doro = request.POST.get('address_doro',None)
        address_jibun = request.POST.get('address_jibun',None)
        address_detail = request.POST.get('address_detail',None)
        phone1 = request.POST.get('phone1',None)
        phone2 = request.POST.get('phone2',None)
        phone3 = request.POST.get('phone3',None)
        
        # email_send = email_certification(request)


        duplicate_check_result = check_duplicate_id(request)

        if 'status' in duplicate_check_result and duplicate_check_result['status'] == 'error':
            # 중복된 ID나올시 error 메세지 처리하는 코드
            return render(request, 'register.html', {'error_message': duplicate_check_result['message']})
        else:
            # 중복이 아닌 경우 계속 진행하도록
            userid = request.POST.get('userid',None)
            user = Userinfo(user_id=userid,
                            user_password=make_password(password),
                            user_name=name,
                            user_gender=gender,
                            user_rrn1=rrn1,
                            user_rrn2=rrn2,
                            user_email=email1+"@"+email2,
                            user_address_num=address_num,
                            user_address_doro=address_doro,
                            user_address_jibun=address_jibun,
                            user_address_detail=address_detail,
                            user_phone=phone1+phone2+phone3,)
                            # user_image_id=img
            
            user.save() # django 에서 db에 저장하는 기능인것같다.
            response = {'status': 'success', 'message': '회원가입이 완료되었습니다.'}
            return HttpResponse(json.dumps(response), content_type='application/json')
    else:
        # GET 요청인 경우 (회원가입창으로 처음 들어올때)
        return render(request, 'register.html')

def login(request):
    if request.method == "GET":
        return render(request, 'main.html')

    elif request.method == "POST":
        loginid = request.POST.get('loginid')
        loginpw = request.POST.get('loginpw')

        try:
            user = Userinfo.objects.get(user_id=loginid)
        except Userinfo.DoesNotExist:
            user = None

        if user is not None and check_password(loginpw, user.user_password):
            auth_login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'ID 혹은 비밀번호 오류입니다. 다시확인해주세요')
            return redirect('/regist/')

verification_codes = {} # 실제 앱에서는 데이터베이스 등으로 하여 사용해야 한다.

@csrf_exempt
def send_code_email(request):
    if request.method == 'POST':
        email = request.POST['email']

        #인증 코드 생성
        code = random.randint(100000,999999)

        #딕셔너리에 인증 코드 저장
        verification_codes[email] = code

        #이메일로 인증 코드 전송
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.starttls()
        smtp.login( settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        msg = MIMEText('당신의 인증번호는 ' + str(code))
        msg['Subject'] = '이메일 인증번호'
        msg['From'] = settings.EMAIL_HOST_USER
        msg['To'] = email
        smtp.send_message(msg)

        return JsonResponse({'status' : 'success'})
    
    return JsonResponse({'status' : 'error', 'message': '잘못된 요청입니다.'})

@csrf_exempt
def verify_code(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # 'email' 키가 없는 경우 None을 반환
        code_str = request.POST.get('code', '')  # 'code' 키가 없는 경우 빈 문자열을 반환

        if not email:
            return JsonResponse({'status': 'error', 'message': '이메일이 제공되지 않았습니다.'})
        if not code_str:
            return JsonResponse({'status': 'error', 'message': '코드가 제공되지 않았습니다.'})

        try:
            code = int(code_str)
        except ValueError:
            return JsonResponse({'status': 'error', 'message': '제공된 코드가 유효하지 않습니다.'})

        # 딕셔너리에서 인증 코드 가져오기
        correct_code = verification_codes.get(email)

        # 인증 코드 확인
        if correct_code is not None and correct_code == code:
            # 인증 성공
            return JsonResponse({'status': 'success', 'message': '인증 성공!'})
        else:
            # 인증 실패
            return JsonResponse({'status': 'error', 'message': '코드가 일치하지 않습니다.'})

    return JsonResponse({'status': 'error', 'message': '잘못된 요청입니다.'})
