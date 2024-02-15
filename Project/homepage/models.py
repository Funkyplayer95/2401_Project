from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# 유저정보 db저장
class Userinfo(models.Model):
    user_id = models.CharField(primary_key=True, max_length=100)
    user_password = models.CharField(max_length=100)
    user_name = models.CharField(unique=True, max_length=100)
    user_gender = models.CharField(max_length=1)
    user_rrn1 = models.IntegerField()
    user_rrn2 = models.IntegerField()
    user_email = models.CharField(unique=True, max_length=100)
    user_address_num = models.IntegerField()
    user_address_doro = models.CharField(max_length=100, blank=True, null=True)
    user_address_jibun = models.CharField(max_length=100, blank=True, null=True)
    user_address_detail = models.CharField(max_length=100, blank=True, null=True)
    user_phone = models.CharField(max_length=100)
    image_extension = models.CharField(max_length=255, blank=True, null=True)
    profile_image = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userinfo'

# 유저 이미지 <아직 작동 x>
class Userimage(models.Model):
    image_id = models.AutoField(primary_key=True)  # 기본키
    image_name = models.CharField(max_length=255)
    image_type = models.CharField(max_length=100)
    image_data = models.BinaryField()
    upload_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userimage'

# 날씨 api db 가져오기
class Cityweather(models.Model):
    city_name = models.CharField(max_length=100, primary_key=True)

    class Meta:
        managed = False
        db_table = 'cityweather'
    def _str_(self): #메인에 DB에 저장되어있는 이름이 표시되도록 함
        return self.name
    

# class Userimg(models.Model):
    

    # def __str__(self):
    #     return self.user_id

# inspectdb 사용해서 db조회할 것
# IntegerField 는 max_length를 할 필요가 없다고 한다.
# ImageField를 사용할꺼면 -m pip install Pillow를 다운받아야 한다고 한다. 물론 적용해보면 터미널에 error와 해결방법이 뜬다.
# 모델의 업데이트 적용을 위해 makemigrations를 진행하고, migrate를 진행해서 정보를 업데이트 시켜야한다.