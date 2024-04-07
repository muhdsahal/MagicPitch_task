from rest_framework import serializers
from .models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','password','referral_code','registred_at']
        extra_kwargs = {
            'password': {'write_only': True},  
            'referral_code': {'read_only': True},
            'registred_at':{'read_only':True}
        }


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','referral_code','registred_at']


class UserReferralSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'registred_at']
