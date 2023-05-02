from rest_framework import generics
from django.contrib.auth.models import User
from . import serializers
from .models import *
from .serializers import SER_Blog_LDC
from rest_framework.decorators import api_view
from rest_framework.response import Response


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
            'img':ch.img,
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
        'img': ch.img,
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
            'img': ch.img,
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