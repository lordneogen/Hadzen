from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


class SER_User(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class SER_Chanell(serializers.ModelSerializer):
    class Meta:
        model = Ch
        fields = '__all__'

class SER_Blog(serializers.ModelSerializer):

    class Meta:
        model = Bl
        fields = '__all__'

class SER_Blog_LDS_all(serializers.ModelSerializer):
    class Meta:
        model = LikeDisShareBl
        fields = '__all__'

class SER_Comm_LD_all(serializers.ModelSerializer):
    class Meta:
        model = LikeDisComm
        fields = '__all__'

class SER_Subs(serializers.ModelSerializer):
    class Meta:
        model = Subs
        fields = '__all__'

class SER_Blog_LDC(serializers.Serializer):
    count = serializers.IntegerField()

class SER_Subs_COUNT(serializers.Serializer):
    count = serializers.IntegerField()

class SER_Manag(serializers.ModelSerializer):

    class Meta:
        model = Manager
        fields = '__all__'

class SER_Comm(serializers.ModelSerializer):

    class Meta:
        model = Comm
        fields = '__all__'

class LDC(serializers.ModelSerializer):
    class Meta:
        model = LikeDisComm
        fields = '__all__'

from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
