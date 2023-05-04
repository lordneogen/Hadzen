from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny

from . import serializers
from .models import *
from .serializers import SER_Blog_LDC,RegisterSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

class LIST_User(generics.ListAPIView, generics.RetrieveAPIView):
    queryset =  User.objects.all()
    serializer_class = serializers.SER_User

    def list(self, request, *args, **kwargs):
        pk=kwargs.get('id')
        if pk:
            queryset = User.objects.filter(pk=pk)
        else:
            queryset = self.get_queryset()
        serializer = serializers.SER_User(data=queryset, many=True)
        if serializer.is_valid():
            return {'error':'not have users'}
        return Response(serializer.data)
    def post(self, request, *args, **kwargs):
        ser = serializers.SER_User(data=request.data)
        if ser.is_valid():
            ser.save()
        return Response(ser.data)
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('id')
        if pk==None:
            return Response("Обьекта не сущетсвует в списке")
        obj = User.objects.get(pk=pk)
        obj.delete()
        return Response("Item succsesfully delete!")
    def put(self, request, *args, **kwargs):
        pk = kwargs.get('id')
        obj = User.objects.get(id=pk)
        ser = serializers.SER_User(instance=obj, data=request.data)
        if ser.is_valid():
            ser.save()
        return Response(ser.data)


class LIST_Chenel(generics.ListAPIView):
    queryset = Ch.objects.all().order_by('-date')
    serializer_class = serializers.SER_Chanell


    def list(self, request, *args, **kwargs):
        pk=kwargs.get('id')
        if pk:
            queryset = Ch.objects.filter(pk=pk).order_by('-date')
        else:
            queryset = self.get_queryset()
        serializer = serializers.SER_Chanell(data=queryset, many=True)
        if serializer.is_valid():
            return {'error':'not have users'}
        return Response(serializer.data)
    def post(self, request, *args, **kwargs):
        ser = serializers.SER_Chanell(data=request.data)
        if ser.is_valid():
            ser.save()
        return Response(ser.data)
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('id')
        if pk==None:
            return Response("Обьекта не сущетсвует в списке")
        obj = Ch.objects.get(pk=pk)
        obj.delete()
        return Response("Item succsesfully delete!")
    def put(self, request, *args, **kwargs):
        pk = kwargs.get('id')
        obj = Ch.objects.get(id=pk)
        ser = serializers.SER_Chanell(instance=obj, data=request.data)
        if ser.is_valid():
            ser.save()
        return Response(ser.data)


class LIST_Blog(generics.ListAPIView):
    queryset = Bl.objects.all().order_by('-date')
    serializer_class = serializers.SER_Blog


    def list(self, request, *args, **kwargs):
        pk=kwargs.get('id')
        if pk:
            queryset = Bl.objects.filter(pk=pk).order_by('-date')
        else:
            queryset = self.get_queryset()
        serializer = serializers.SER_Blog(data=queryset, many=True)
        if serializer.is_valid():
            return {'error':'not have users'}
        return Response(serializer.data)
    def post(self, request, *args, **kwargs):
        ser = serializers.SER_Blog(data=request.data)
        if ser.is_valid():
            ser.save()
        return Response(ser.data)
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('id')
        if pk==None:
            return Response("Обьекта не сущетсвует в списке")
        obj = Bl.objects.get(pk=pk)
        obj.delete()
        return Response("Item succsesfully delete!")
    def put(self, request, *args, **kwargs):
        pk = kwargs.get('id')
        obj = Bl.objects.get(id=pk)
        ser = serializers.SER_Blog(instance=obj, data=request.data)
        if ser.is_valid():
            ser.save()
        return Response(ser.data)


class LIST_Blog_LDS(generics.ListAPIView):
    queryset = LikeDisShareBl.objects.all()
    serializer_class = serializers.SER_Blog_LDS_all

    def list(self, request, *args, **kwargs):
        pk = kwargs.get('id')
        if pk:
            queryset =LikeDisShareBl.objects.filter(pk=pk).order_by('bl')
        else:
            queryset = self.get_queryset()
        serializer = serializers.SER_Blog_LDS_all(data=queryset, many=True)
        if serializer.is_valid():
            return {'error': 'not have users'}
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        ser = serializers.SER_Blog_LDS_all(data=request.data)
        if ser.is_valid():
            ser.save()
        return Response(ser.data)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('id')
        if pk == None:
            return Response("Обьекта не сущетсвует в списке")
        obj = LikeDisShareBl.objects.get(pk=pk)
        obj.delete()
        return Response("Item succsesfully delete!")

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('id')
        obj = LikeDisShareBl.objects.get(id=pk)
        ser = serializers.SER_Blog_LDS_all(instance=obj, data=request.data)
        if ser.is_valid():
            ser.save()
        return Response(ser.data)


class LIST_Comm_LDS(generics.ListAPIView):
    queryset = LikeDisComm.objects.all()
    serializer_class = serializers.SER_Comm_LD_all

    def list(self, request, *args, **kwargs):
        pk = kwargs.get('id')
        if pk:
            queryset =LikeDisComm.objects.filter(pk=pk).order_by('bl')
        else:
            queryset = self.get_queryset()
        serializer = serializers.SER_Comm_LD_all(data=queryset, many=True)
        if serializer.is_valid():
            return {'error': 'not have users'}
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        ser = serializers.SER_Comm_LD_all(data=request.data)
        if ser.is_valid():
            ser.save()
        return Response(ser.data)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('id')
        if pk == None:
            return Response("Обьекта не сущетсвует в списке")
        obj = LikeDisComm.objects.get(pk=pk)
        obj.delete()
        return Response("Item succsesfully delete!")

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('id')
        obj = LikeDisComm.objects.get(id=pk)
        ser = serializers.SER_Comm_LD_all(instance=obj, data=request.data)
        if ser.is_valid():
            ser.save()
        return Response(ser.data)

class LIST_Comm(generics.ListAPIView):
    queryset = Comm.objects.all()
    serializer_class = serializers.SER_Comm

    def list(self, request, *args, **kwargs):
        pk = kwargs.get('id')
        if pk:
            queryset =Comm.objects.filter(pk=pk).order_by('bl')
        else:
            queryset = self.get_queryset()
        serializer = serializers.SER_Comm(data=queryset, many=True)
        if serializer.is_valid():
            return {'error': 'not have users'}
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        ser = serializers.SER_Comm(data=request.data)
        if ser.is_valid():
            ser.save()
        return Response(ser.data)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('id')
        if pk == None:
            return Response("Обьекта не сущетсвует в списке")
        obj = Comm.objects.get(pk=pk)
        obj.delete()
        return Response("Item succsesfully delete!")

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('id')
        obj = Comm.objects.get(id=pk)
        ser = serializers.SER_Comm(instance=obj, data=request.data)
        if ser.is_valid():
            ser.save()
        return Response(ser.data)

class LIST_Manager(generics.ListAPIView):
    queryset = Manager.objects.all().order_by('-email')
    serializer_class = serializers.SER_Manag

    def list(self, request, *args, **kwargs):
        pk=kwargs.get('id')
        if pk:
            queryset =  Manager.objects.filter(pk=pk).order_by('-email')
        else:
            queryset = self.get_queryset()
        serializer = serializers.SER_Manag(data=queryset, many=True)
        if serializer.is_valid():
            return {'error':'not have users'}
        return Response(serializer.data)
    def post(self, request, *args, **kwargs):
        ser = serializers.SER_Manag(data=request.data)
        if ser.is_valid():
            ser.save()
        return Response(ser.data)
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('id')
        if pk==None:
            return Response("Обьекта не сущетсвует в списке")
        obj = Manager.objects.get(pk=pk)
        obj.delete()
        return Response("Item succsesfully delete!")
    def update(self, request, *args, **kwargs):
        pk = kwargs.get('id')
        obj = Manager.objects.get(id=pk)
        ser = serializers.SER_Manag(instance=obj, data=request.data)
        if ser.is_valid():
            ser.save()
        return Response(ser.data)


class LIST_Subs(generics.ListAPIView):
    queryset = Subs.objects.all()
    serializer_class = serializers.SER_Subs

    def list(self, request, *args, **kwargs):
        pk = kwargs.get('id')
        if pk:
            queryset = Subs.objects.filter(pk=pk)
        else:
            queryset = self.get_queryset()
        serializer = serializers.SER_Subs(data=queryset, many=True)
        if serializer.is_valid():
            return {'error': 'not have users'}
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        ser = serializers.SER_Subs(data=request.data)
        if ser.is_valid():
            ser.save()
        return Response(ser.data)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('id')
        if pk == None:
            return Response("Обьекта не сущетсвует в списке")
        obj = Subs.objects.get(pk=pk)
        obj.delete()
        return Response("Item succsesfully delete!")

    def update(self, request, *args, **kwargs):
        pk = kwargs.get('id')
        obj = Subs.objects.get(id=pk)
        ser = serializers.SER_Subs(instance=obj, data=request.data)
        if ser.is_valid():
            ser.save()
        return Response(ser.data)



class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer