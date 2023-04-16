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
