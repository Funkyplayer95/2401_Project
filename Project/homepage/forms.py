from django import forms
from .models import Userinfo

class UserinfoForm(forms.ModelForm):
    class Meta:
        model = Userinfo
        fields = ['user_id', 'user_password', 'user_name', 'user_gender', 'user_rrn1', 'user_rrn2', 'user_email',
                  'user_address_num', 'user_address_doro', 'user_address_jibun', 'user_address_detail', 'user_image_id']

class UploadImageForm(forms.ModelForm):
    class Meta:
        model = Userinfo
        fields = ['user_image_id']