from rest_framework import serializers
from .models import Userinfo

class withSpring(serializers.ModelSerializer):
    class Meta:
        model = Userinfo
        fields = '__all__'  # 모든 필드를 포함
