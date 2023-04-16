from rest_framework import generics
from django.contrib.auth.models import User
from . import serializers
from .models import *
from .serializers import SER_Blog_LDC
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


@api_view(['GET'])
def BLOG_LIKE(request, id):
    count = LikeDisShareBl.objects.filter(bl=id,is_like=True).count()
    serializer_new = SER_Blog_LDC({'count': count})
    return Response(serializer_new.data)


@api_view(['GET'])
def ALL_BLOGS(request):

    obj = Bl.objects.all().order_by('-date')
    data=[]
    for x in obj:
        count = Subs.objects.filter(ch=x.ch.pk).count()
        serializer_new1 = serializers.SER_Subs_COUNT({'count': count})
        id=x.pk
        blog = Bl.objects.get(id=x.pk)
        ch = blog.ch
        # получение количества лайков
        like_count = LikeDisShareBl.objects.filter(bl=id, is_like=True).count()
        dislike_count = LikeDisShareBl.objects.filter(bl=id, is_dis=True).count()
        share_count = LikeDisShareBl.objects.filter(bl=id, is_share=True).count()
        # сериализация объекта блога
        blog_serializer = serializers.SER_Blog(blog)

        # создание словаря с данными
        response_data = {
            'chanell': ch.name,
            'subs': serializer_new1.data["count"],
            'blog_details': blog_serializer.data,
            'like_count': like_count,
            'dis_count': dislike_count,
            'share_count': share_count
        }
        data.append(response_data)
    return Response(data)

@api_view(['GET'])
def CHENELL_DETAIL(request, id):
    obj = Bl.objects.filter(ch=id).order_by('-date')
    data=[]
    for x in obj:
        blog = Bl.objects.get(id=x.pk)

        # получение количества лайков
        like_count = LikeDisShareBl.objects.filter(bl=id, is_like=True).count()
        dislike_count = LikeDisShareBl.objects.filter(bl=id, is_dis=True).count()
        share_count = LikeDisShareBl.objects.filter(bl=id, is_share=True).count()
        # сериализация объекта блога
        blog_serializer = serializers.SER_Blog(blog)

        # создание словаря с данными
        response_data = {

            'blog_details': blog_serializer.data,
            'like_count': like_count,
            'dis_count': dislike_count,
            'share_count': share_count
        }
        data.append(response_data)
    return Response(data)

@api_view(['GET'])
def BLOG_DETAIL(request, id):
    comments_list=[]
    comments=Comm.objects.filter(bl=id).order_by('-date')
    for x in comments:
        print(x.user.username)
        dt=serializers.SER_Comm(x).data
        lk=LikeDisComm.objects.filter(comm=x.id, is_like=True).count()
        ds = LikeDisComm.objects.filter(comm=x.id, is_dis=True).count()
        comments_list.append({
            "user":x.user.username,
            "text":dt["text"],
            "date":dt["date"],
            "like":lk,
            "dis":ds
        })
    count = Subs.objects.filter(ch=id).count()
    serializer_new1 = serializers.SER_Subs_COUNT({'count': count})
    # получение объекта блога
    blog = Bl.objects.get(id=id)
    ch=blog.ch
    # ch=Ch.objects.get(blog.ch)
    # получение количества лайков
    like_count = LikeDisShareBl.objects.filter(bl=id, is_like=True).count()
    dislike_count = LikeDisShareBl.objects.filter(bl=id, is_dis=True).count()
    share_count = LikeDisShareBl.objects.filter(bl=id, is_share=True).count()
    # сериализация объекта блога
    blog_serializer = serializers.SER_Blog(blog)

    # создание словаря с данными
    response_data = {
        'chanell':ch.name,
        'subs':serializer_new1.data["count"],
        'blog_details': blog_serializer.data,
        'like_count': like_count,
        'dis_count':dislike_count,
        'share_count':share_count,
        'comments':comments_list
    }

    # отправка ответа
    return Response(response_data)

@api_view(['GET'])
def CHENELL_SUBS(request, id):
    count = Subs.objects.filter(ch=id).count()
    serializer_new = serializers.SER_Subs_COUNT({'count': count})
    return Response(serializer_new.data)

@api_view(['GET'])
def CHENELL_MANGAER(request, id):
    count = Manager.objects.filter(ch=id)
    objs=[]
    for obj in count:
        ser=serializers.SER_Manag(obj).data
        objs.append(ser)
    return Response(objs)

@api_view(['GET'])
def BLOG_PAGE(request, page):
    page_num=int(page[4:])
    obj = Bl.objects.all().order_by('-date')[(page_num-1)*5:page_num*5]
    data = []
    for x in obj:
        count = Subs.objects.filter(ch=x.pk).count()
        serializer_new1 = serializers.SER_Subs_COUNT({'count': count})
        id = x.pk
        blog = Bl.objects.get(id=x.pk)
        ch = blog.ch
        # получение количества лайков
        like_count = LikeDisShareBl.objects.filter(bl=id, is_like=True).count()
        dislike_count = LikeDisShareBl.objects.filter(bl=id, is_dis=True).count()
        share_count = LikeDisShareBl.objects.filter(bl=id, is_share=True).count()
        # сериализация объекта блога
        blog_serializer = serializers.SER_Blog(blog)

        # создание словаря с данными
        response_data = {
            'chanell': ch.name,
            'subs': serializer_new1.data["count"],
            'blog_details': blog_serializer.data,
            'like_count': like_count,
            'dis_count': dislike_count,
            'share_count': share_count
        }
        data.append(response_data)
    return Response(data)

@api_view(['GET'])
def CH_BLOG_PAGE(request, page, id):
    page_num=int(page[4:])
    obj = Bl.objects.filter(ch=id).order_by('-date')[(page_num-1)*5:page_num*5]
    data = []
    for x in obj:
        count = Subs.objects.filter(ch=x.pk).count()
        serializer_new1 = serializers.SER_Subs_COUNT({'count': count})
        id = x.pk
        blog = Bl.objects.get(id=x.pk)
        ch = blog.ch
        # получение количества лайков
        like_count = LikeDisShareBl.objects.filter(bl=id, is_like=True).count()
        dislike_count = LikeDisShareBl.objects.filter(bl=id, is_dis=True).count()
        share_count = LikeDisShareBl.objects.filter(bl=id, is_share=True).count()
        # сериализация объекта блога
        blog_serializer = serializers.SER_Blog(blog)

        # создание словаря с данными
        response_data = {
            'chanell': ch.name,
            'subs': serializer_new1.data["count"],
            'blog_details': blog_serializer.data,
            'like_count': like_count,
            'dis_count': dislike_count,
            'share_count': share_count
        }
        data.append(response_data)
    return Response(data)
