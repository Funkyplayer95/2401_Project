from django.shortcuts import render, redirect # render = 불러오기 / redirect = 다시 재실행하는
from django.http import JsonResponse, HttpResponse # Json값으로 response하는것 (키 : 벨류)
from django.views.decorators.csrf import csrf_exempt # csrf 충돌을 막기위함이라함. 공부할 것.
from django.contrib import messages # 장고의 messages 프레임워크를 사용한다.
from django.contrib.auth.hashers import make_password, check_password # password 암호화 하기위해 django에서 주는 import
from django.contrib.auth import authenticate,login as auth_login
from .models import Userinfo,Cityweather # 내가 가져올 class import해주기
from django.conf import settings # settings.py 참고 가져오기위해.
import requests
import json
import random #랜덤인증코드 전송을 위해 사용.
import smtplib #이메일 전송 위해
from email.mime.text import MIMEText #이메일 전송 위해
from django.contrib.messages import constants as message_constants
from rest_framework import viewsets
from .serializers import withSpring

# @csrf_exempt는 장고에서 제공하는 데코레이터. cross-site Request Forgery 보호기능을 무시함.
# CSRF는 웹사이트 취약점 공격중 하나. 사용자가 자신의 의지와는 무관하게 공격자가 의도한 행위를 특정 웹 사이트에 요청하게 만드는 공격
# 그래서 장고는 공격을 방어하기 위해서 POST 형식의 요청에 CSRF 토큰을 첨부하여 요청의 유효성을 검증한다.

MESSAGE_LEVEL = message_constants.DEBUG

# 장바구니
def cart(request):
    carts = Userinfo.objects.get(user_id = request.user.user_id).carts.all()
    return render(request, 'mypage.html', {'carts':carts})

########################## 메인 부분 ######################################
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
    
    # 로그인된 사용자의 아이디를 가져온다.
    user_id = request.session.get('user_id')

    # 날씨 api 와 카카오지도 api키를 가져와서 context안에 저장시킴.
    context = {'weather_data' : weather_data , 'kakaoapi' : kakaoapi, 'user_id': user_id} # context안에 작성하면 html에서 {{ }} 로 불러올 수 있음
    print(request.session.get('user_id')) # 저장되어 있는 session의 user_id를 출력해본다.

    return render(request, 'main.html', context) 
#################################################################################

########################## id 중복 부분 ######################################
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
#################################################################################

########################## 회원가입 부분 ######################################
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
            userid = request.POST.get('userid',None) # 아이디는 중복체크 후 진행하기에 이곳에 진행하였다.
            
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
#################################################################################

########################## 로그인 부분 ######################################
def login(request):
    if request.method == 'POST':
        user_id = request.POST['loginid'] # id value값
        user_password = request.POST['loginpw'] # pw value 값
        try:
            user = Userinfo.objects.get(user_id=user_id) # 데이터베이스에 있는 user_id와 비교했을때 id가 일치하는지
            if check_password(user_password, user.user_password): # pw value값과 id가 일치한 데이터베이스의 password가 참이면
                request.session['user_id'] = user_id # 세션의 user_id에 id값을 저장한다
                messages.success(request, '로그인에 성공하였습니다.')  # 로그인 성공 메시지
                return redirect('/')  # 로그인 성공 후 리다이렉션할 페이지
            else:
                # 비밀번호가 틀린 경우
                messages.error(request, '아이디 또는 비밀번호가 잘못되었습니다.') # 메세지 프레임워크에서 오류메세지를 생성하여 진행.
                return redirect('/')
        except Userinfo.DoesNotExist: # userinfo 테이블에 데이터가 존재하지 않을경우
            messages.error(request, '아이디 또는 비밀번호가 잘못되었습니다.')
            return redirect('/')
    else:
        return redirect('/')
    
#################################################################################

########################## 이메일 인증 부분 ######################################
verification_codes = {} # 실제 앱에서는 데이터베이스 등으로 하여 사용해야 한다.. 이건 좀 더 공부해보자.

@csrf_exempt
def send_code_email(request): # 이메일 전송 함수
    if request.method == 'POST':
        email = request.POST['email']

        #인증 코드 생성
        code = random.randint(100000,999999) # 인증코드 6자리를 랜덤으로 진행할 수 있도록 사용.

        #딕셔너리에 인증 코드 저장
        verification_codes[email] = code #verification_codes 딕셔너리에 [email] 을 키로. code(인증코드)를 값으로 저장하는 방법.

        #이메일로 인증 코드 전송
        smtp = smtplib.SMTP('smtp.gmail.com', 587) # smtp 서버에 연결 설정 부분. google stml코드에 587번 포트로 설정
        smtp.starttls() # 보안연결로 업그레이드하는 코드. TLS, SSL 프로토콜로 부터 보호하도록. 전송시 중간에서 가로채거나 수정하는것에 대한 방지.
        smtp.login( settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD) # settings안에서 사용자 이메일, 사용자 앱 비밀번호 사용.
        msg = MIMEText('당신의 인증번호는 ' + str(code)) # 메세지 안에 작성될 내용. 여기서는 str(code)를 사용해서 6자리 인증번호 랜덤생성
        msg['Subject'] = '이메일 인증번호' # 이메일의 제목을 담당하는 부분.
        msg['From'] = settings.EMAIL_HOST_USER # 발송자 부분을 설정하는 부분.
        msg['To'] = email # 수신자를 설정하는 코드
        smtp.send_message(msg) # 위에서 만든 설정대로 메일을 보냄.

        return JsonResponse({'status' : 'success'}) # 상태에 성공을 보낸다.
    
    return JsonResponse({'status' : 'error', 'message': '잘못된 요청입니다.'}) # 상태에 error를 보내고 잘못된요청이라는 메세지 출력

@csrf_exempt
def verify_code(request): # 인증코드 확인하는 
    if request.method == 'POST':
        email = request.POST.get('email')  # 'email' 키가 없는 경우 None을 반환
        code_str = request.POST.get('code', '')  # 'code' 키가 없는 경우 빈 문자열을 반환

        if not email: # 이메일 값이 제공 되지 않을 경우
            return JsonResponse({'status': 'error', 'message': '이메일이 제공되지 않았습니다.'})
        if not code_str: # 인증코드 값이 제공 되지 않을 경우
            return JsonResponse({'status': 'error', 'message': '코드가 제공되지 않았습니다.'})

        try:
            code = int(code_str) # 인증코드값을 int로 변경해준다.
        except ValueError: # 정수로 변할 수 없는 문자열이라면
            return JsonResponse({'status': 'error', 'message': '제공된 코드가 유효하지 않습니다.'}) # 에러로 진행.

        # 딕셔너리에서 인증 코드 가져오기
        correct_code = verification_codes.get(email) # verification_codes에서 저장되있던 인증코드를 가져오는 것. 값이없으면 none으로.

        # 인증 코드 확인
        if correct_code is not None and correct_code == code: # 빈값이 아니고 작성된 code가 저장되있던 코드와 같다면
            # 인증 성공
            return JsonResponse({'status': 'success', 'message': '인증 성공!'})
        else:
            # 인증 실패
            return JsonResponse({'status': 'error', 'message': '코드가 일치하지 않습니다.'})

    return JsonResponse({'status': 'error', 'message': '잘못된 요청입니다.'})
#################################################################################

class ModelViewSet(viewsets.ModelViewSet):
    queryset = Userinfo.objects.all()
    serializer_class = withSpring